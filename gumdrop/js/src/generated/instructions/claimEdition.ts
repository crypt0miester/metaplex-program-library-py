/**
 * This code was GENERATED using the solita package.
 * Please DO NOT EDIT THIS FILE, instead rerun solita to update it or write a wrapper to add functionality.
 *
 * See: https://github.com/metaplex-foundation/solita
 */

import * as splToken from '@solana/spl-token';
import * as beet from '@metaplex-foundation/beet';
import * as web3 from '@solana/web3.js';
import * as beetSolana from '@metaplex-foundation/beet-solana';

/**
 * @category Instructions
 * @category ClaimEdition
 * @category generated
 */
export type ClaimEditionInstructionArgs = {
  claimBump: number;
  index: beet.bignum;
  amount: beet.bignum;
  edition: beet.bignum;
  claimantSecret: web3.PublicKey;
  proof: number[] /* size: 32 */[];
};
/**
 * @category Instructions
 * @category ClaimEdition
 * @category generated
 */
const claimEditionStruct = new beet.FixableBeetArgsStruct<
  ClaimEditionInstructionArgs & {
    instructionDiscriminator: number[] /* size: 8 */;
  }
>(
  [
    ['instructionDiscriminator', beet.uniformFixedSizeArray(beet.u8, 8)],
    ['claimBump', beet.u8],
    ['index', beet.u64],
    ['amount', beet.u64],
    ['edition', beet.u64],
    ['claimantSecret', beetSolana.publicKey],
    ['proof', beet.array(beet.uniformFixedSizeArray(beet.u8, 32))],
  ],
  'ClaimEditionInstructionArgs',
);
/**
 * Accounts required by the _claimEdition_ instruction
 * @category Instructions
 * @category ClaimEdition
 * @category generated
 */
export type ClaimEditionInstructionAccounts = {
  distributor: web3.PublicKey;
  claimCount: web3.PublicKey;
  temporal: web3.PublicKey;
  payer: web3.PublicKey;
  metadataNewMetadata: web3.PublicKey;
  metadataNewEdition: web3.PublicKey;
  metadataMasterEdition: web3.PublicKey;
  metadataNewMint: web3.PublicKey;
  metadataEditionMarkPda: web3.PublicKey;
  metadataNewMintAuthority: web3.PublicKey;
  metadataMasterTokenAccount: web3.PublicKey;
  metadataNewUpdateAuthority: web3.PublicKey;
  metadataMasterMetadata: web3.PublicKey;
  metadataMasterMint: web3.PublicKey;
  tokenMetadataProgram: web3.PublicKey;
};

const claimEditionInstructionDiscriminator = [150, 83, 124, 180, 53, 35, 144, 248];

/**
 * Creates a _ClaimEdition_ instruction.
 *
 * @param accounts that will be accessed while the instruction is processed
 * @param args to provide as instruction data to the program
 *
 * @category Instructions
 * @category ClaimEdition
 * @category generated
 */
export function createClaimEditionInstruction(
  accounts: ClaimEditionInstructionAccounts,
  args: ClaimEditionInstructionArgs,
) {
  const {
    distributor,
    claimCount,
    temporal,
    payer,
    metadataNewMetadata,
    metadataNewEdition,
    metadataMasterEdition,
    metadataNewMint,
    metadataEditionMarkPda,
    metadataNewMintAuthority,
    metadataMasterTokenAccount,
    metadataNewUpdateAuthority,
    metadataMasterMetadata,
    metadataMasterMint,
    tokenMetadataProgram,
  } = accounts;

  const [data] = claimEditionStruct.serialize({
    instructionDiscriminator: claimEditionInstructionDiscriminator,
    ...args,
  });
  const keys: web3.AccountMeta[] = [
    {
      pubkey: distributor,
      isWritable: true,
      isSigner: false,
    },
    {
      pubkey: claimCount,
      isWritable: true,
      isSigner: false,
    },
    {
      pubkey: temporal,
      isWritable: false,
      isSigner: true,
    },
    {
      pubkey: payer,
      isWritable: false,
      isSigner: true,
    },
    {
      pubkey: metadataNewMetadata,
      isWritable: true,
      isSigner: false,
    },
    {
      pubkey: metadataNewEdition,
      isWritable: true,
      isSigner: false,
    },
    {
      pubkey: metadataMasterEdition,
      isWritable: true,
      isSigner: false,
    },
    {
      pubkey: metadataNewMint,
      isWritable: true,
      isSigner: false,
    },
    {
      pubkey: metadataEditionMarkPda,
      isWritable: true,
      isSigner: false,
    },
    {
      pubkey: metadataNewMintAuthority,
      isWritable: false,
      isSigner: true,
    },
    {
      pubkey: metadataMasterTokenAccount,
      isWritable: false,
      isSigner: false,
    },
    {
      pubkey: metadataNewUpdateAuthority,
      isWritable: false,
      isSigner: false,
    },
    {
      pubkey: metadataMasterMetadata,
      isWritable: false,
      isSigner: false,
    },
    {
      pubkey: metadataMasterMint,
      isWritable: false,
      isSigner: false,
    },
    {
      pubkey: web3.SystemProgram.programId,
      isWritable: false,
      isSigner: false,
    },
    {
      pubkey: splToken.TOKEN_PROGRAM_ID,
      isWritable: false,
      isSigner: false,
    },
    {
      pubkey: tokenMetadataProgram,
      isWritable: false,
      isSigner: false,
    },
    {
      pubkey: web3.SYSVAR_RENT_PUBKEY,
      isWritable: false,
      isSigner: false,
    },
  ];

  const ix = new web3.TransactionInstruction({
    programId: new web3.PublicKey('gdrpGjVffourzkdDRrQmySw4aTHr8a3xmQzzxSwFD1a'),
    keys,
    data,
  });
  return ix;
}
