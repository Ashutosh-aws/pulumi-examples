// Code adapted from https://github.com/jen20/pulumi-aws-vpc/blob/master/nodejs/src/subnetDistributor.ts
// and used in accordance with MPL v2.0 license


/**
 * A SubnetDistributor is used to split a given CIDR block into a number of
 * subnets.
 */
 export class SubnetDistributor {
    private readonly _privateSubnets: string[];
    private readonly _publicSubnets: string[];

    /**
     * Returns a subnet distributor configured to split the baseCidr into a fixed
     * number of public/private subnet pairs.
     * @param {string} baseCidr The CIDR block to split.
     * @param {number} adCount The number of subnet pairs to produce.
     */
    public constructor(baseCidr: string, adCount: number) {
        const newBitsPerAZ = Math.log2(nextPow2(adCount));

        const azBases: string[] = [];
        for (let i = 0; i < adCount; i++) {
            azBases.push(cidrSubnetV4(baseCidr, newBitsPerAZ, i));
        }

        this._privateSubnets = azBases.map((block) => {
            return cidrSubnetV4(block, 1, 0);
        });

        this._publicSubnets = this._privateSubnets.map((block) => {
            const splitBase = cidrSubnetV4(block, 0, 1);
            return cidrSubnetV4(splitBase, 1, 0);
        });
    }

    /**
     * Returns an array of the CIDR blocks for the private subnets.
     * @returns {string[]}
     */
    public privateSubnets(): string[] {
        return this._privateSubnets;
    }

    /**
     * Returns an array of the CIDR blocks for the public subnets.
     * @returns {string[]}
     */
    public publicSubnets(): string[] {
        return this._publicSubnets;
    }
}

function cidrSubnetV4(ipRange: string, newBits: number, netNum: number): string {
    const ipAddress = require("ip-address");
    const BigInteger = require("jsbn").BigInteger;

    const ipv4 = new ipAddress.Address4(ipRange);

    const newSubnetMask = ipv4.subnetMask + newBits;
    if (newSubnetMask > 32) {
        throw new Error(`Requested ${newBits} new bits, but ` +
            `only ${32 - ipv4.subnetMask} are available.`);
    }

    const addressBI = ipv4.bigInteger();
    const newAddressBase = Math.pow(2, 32 - newSubnetMask);
    const netNumBI = new BigInteger(netNum.toString());

    const newAddressBI = addressBI.add(new BigInteger(newAddressBase.toString()).multiply(netNumBI));
    const newAddress = ipAddress.Address4.fromBigInteger(newAddressBI).address;

    return `${newAddress}/${newSubnetMask}`;
}

/**
 * nextPow2 returns the next integer greater or equal to n which is a power of 2.
 * @param {number} n input number
 * @returns {number} next power of 2 to n (>= n)
 */
function nextPow2(n: number): number {
    if (n === 0) {
        return 1;
    }

    n--;
    n |= n >> 1;
    n |= n >> 2;
    n |= n >> 4;
    n |= n >> 8;
    n |= n >> 16;

    return n + 1;
}