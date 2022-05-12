import typing
from anchorpy.error import ProgramError


class InstructionUnpackError(ProgramError):
    def __init__(self) -> None:
        super().__init__(0, "Failed to unpack instruction data")

    code = 0
    name = "InstructionUnpackError"
    msg = "Failed to unpack instruction data"


class InstructionPackError(ProgramError):
    def __init__(self) -> None:
        super().__init__(1, "Failed to pack instruction data")

    code = 1
    name = "InstructionPackError"
    msg = "Failed to pack instruction data"


class NotRentExempt(ProgramError):
    def __init__(self) -> None:
        super().__init__(2, "Lamport balance below rent-exempt threshold")

    code = 2
    name = "NotRentExempt"
    msg = "Lamport balance below rent-exempt threshold"


class AlreadyInitialized(ProgramError):
    def __init__(self) -> None:
        super().__init__(3, "Already initialized")

    code = 3
    name = "AlreadyInitialized"
    msg = "Already initialized"


class Uninitialized(ProgramError):
    def __init__(self) -> None:
        super().__init__(4, "Uninitialized")

    code = 4
    name = "Uninitialized"
    msg = "Uninitialized"


class InvalidMetadataKey(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            5,
            " Metadata's key must match seed of ['metadata', program id, mint] provided",
        )

    code = 5
    name = "InvalidMetadataKey"
    msg = " Metadata's key must match seed of ['metadata', program id, mint] provided"


class InvalidEditionKey(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6,
            "Edition's key must match seed of ['metadata', program id, name, 'edition'] provided",
        )

    code = 6
    name = "InvalidEditionKey"
    msg = "Edition's key must match seed of ['metadata', program id, name, 'edition'] provided"


class UpdateAuthorityIncorrect(ProgramError):
    def __init__(self) -> None:
        super().__init__(7, "Update Authority given does not match")

    code = 7
    name = "UpdateAuthorityIncorrect"
    msg = "Update Authority given does not match"


class UpdateAuthorityIsNotSigner(ProgramError):
    def __init__(self) -> None:
        super().__init__(8, "Update Authority needs to be signer to update metadata")

    code = 8
    name = "UpdateAuthorityIsNotSigner"
    msg = "Update Authority needs to be signer to update metadata"


class NotMintAuthority(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            9, "You must be the mint authority and signer on this transaction"
        )

    code = 9
    name = "NotMintAuthority"
    msg = "You must be the mint authority and signer on this transaction"


class InvalidMintAuthority(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            10, "Mint authority provided does not match the authority on the mint"
        )

    code = 10
    name = "InvalidMintAuthority"
    msg = "Mint authority provided does not match the authority on the mint"


class NameTooLong(ProgramError):
    def __init__(self) -> None:
        super().__init__(11, "Name too long")

    code = 11
    name = "NameTooLong"
    msg = "Name too long"


class SymbolTooLong(ProgramError):
    def __init__(self) -> None:
        super().__init__(12, "Symbol too long")

    code = 12
    name = "SymbolTooLong"
    msg = "Symbol too long"


class UriTooLong(ProgramError):
    def __init__(self) -> None:
        super().__init__(13, "URI too long")

    code = 13
    name = "UriTooLong"
    msg = "URI too long"


class UpdateAuthorityMustBeEqualToMetadataAuthorityAndSigner(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            14,
            "Update authority must be equivalent to the metadata's authority and also signer of this transaction",
        )

    code = 14
    name = "UpdateAuthorityMustBeEqualToMetadataAuthorityAndSigner"
    msg = "Update authority must be equivalent to the metadata's authority and also signer of this transaction"


class MintMismatch(ProgramError):
    def __init__(self) -> None:
        super().__init__(15, "Mint given does not match mint on Metadata")

    code = 15
    name = "MintMismatch"
    msg = "Mint given does not match mint on Metadata"


class EditionsMustHaveExactlyOneToken(ProgramError):
    def __init__(self) -> None:
        super().__init__(16, "Editions must have exactly one token")

    code = 16
    name = "EditionsMustHaveExactlyOneToken"
    msg = "Editions must have exactly one token"


class MaxEditionsMintedAlready(ProgramError):
    def __init__(self) -> None:
        super().__init__(17, "Maximum editions printed already")

    code = 17
    name = "MaxEditionsMintedAlready"
    msg = "Maximum editions printed already"


class TokenMintToFailed(ProgramError):
    def __init__(self) -> None:
        super().__init__(18, "Token mint to failed")

    code = 18
    name = "TokenMintToFailed"
    msg = "Token mint to failed"


class MasterRecordMismatch(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            19,
            "The master edition record passed must match the master record on the edition given",
        )

    code = 19
    name = "MasterRecordMismatch"
    msg = "The master edition record passed must match the master record on the edition given"


class DestinationMintMismatch(ProgramError):
    def __init__(self) -> None:
        super().__init__(20, "The destination account does not have the right mint")

    code = 20
    name = "DestinationMintMismatch"
    msg = "The destination account does not have the right mint"


class EditionAlreadyMinted(ProgramError):
    def __init__(self) -> None:
        super().__init__(21, "An edition can only mint one of its kind!")

    code = 21
    name = "EditionAlreadyMinted"
    msg = "An edition can only mint one of its kind!"


class PrintingMintDecimalsShouldBeZero(ProgramError):
    def __init__(self) -> None:
        super().__init__(22, "Printing mint decimals should be zero")

    code = 22
    name = "PrintingMintDecimalsShouldBeZero"
    msg = "Printing mint decimals should be zero"


class OneTimePrintingAuthorizationMintDecimalsShouldBeZero(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            23, "OneTimePrintingAuthorization mint decimals should be zero"
        )

    code = 23
    name = "OneTimePrintingAuthorizationMintDecimalsShouldBeZero"
    msg = "OneTimePrintingAuthorization mint decimals should be zero"


class EditionMintDecimalsShouldBeZero(ProgramError):
    def __init__(self) -> None:
        super().__init__(24, "EditionMintDecimalsShouldBeZero")

    code = 24
    name = "EditionMintDecimalsShouldBeZero"
    msg = "EditionMintDecimalsShouldBeZero"


class TokenBurnFailed(ProgramError):
    def __init__(self) -> None:
        super().__init__(25, "Token burn failed")

    code = 25
    name = "TokenBurnFailed"
    msg = "Token burn failed"


class TokenAccountOneTimeAuthMintMismatch(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            26,
            "The One Time authorization mint does not match that on the token account!",
        )

    code = 26
    name = "TokenAccountOneTimeAuthMintMismatch"
    msg = "The One Time authorization mint does not match that on the token account!"


class DerivedKeyInvalid(ProgramError):
    def __init__(self) -> None:
        super().__init__(27, "Derived key invalid")

    code = 27
    name = "DerivedKeyInvalid"
    msg = "Derived key invalid"


class PrintingMintMismatch(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            28, "The Printing mint does not match that on the master edition!"
        )

    code = 28
    name = "PrintingMintMismatch"
    msg = "The Printing mint does not match that on the master edition!"


class OneTimePrintingAuthMintMismatch(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            29,
            "The One Time Printing Auth mint does not match that on the master edition!",
        )

    code = 29
    name = "OneTimePrintingAuthMintMismatch"
    msg = "The One Time Printing Auth mint does not match that on the master edition!"


class TokenAccountMintMismatch(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            30, "The mint of the token account does not match the Printing mint!"
        )

    code = 30
    name = "TokenAccountMintMismatch"
    msg = "The mint of the token account does not match the Printing mint!"


class TokenAccountMintMismatchV2(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            31, "The mint of the token account does not match the master metadata mint!"
        )

    code = 31
    name = "TokenAccountMintMismatchV2"
    msg = "The mint of the token account does not match the master metadata mint!"


class NotEnoughTokens(ProgramError):
    def __init__(self) -> None:
        super().__init__(32, "Not enough tokens to mint a limited edition")

    code = 32
    name = "NotEnoughTokens"
    msg = "Not enough tokens to mint a limited edition"


class PrintingMintAuthorizationAccountMismatch(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            33,
            "The mint on your authorization token holding account does not match your Printing mint!",
        )

    code = 33
    name = "PrintingMintAuthorizationAccountMismatch"
    msg = "The mint on your authorization token holding account does not match your Printing mint!"


class AuthorizationTokenAccountOwnerMismatch(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            34,
            "The authorization token account has a different owner than the update authority for the master edition!",
        )

    code = 34
    name = "AuthorizationTokenAccountOwnerMismatch"
    msg = "The authorization token account has a different owner than the update authority for the master edition!"


class Disabled(ProgramError):
    def __init__(self) -> None:
        super().__init__(35, "This feature is currently disabled.")

    code = 35
    name = "Disabled"
    msg = "This feature is currently disabled."


class CreatorsTooLong(ProgramError):
    def __init__(self) -> None:
        super().__init__(36, "Creators list too long")

    code = 36
    name = "CreatorsTooLong"
    msg = "Creators list too long"


class CreatorsMustBeAtleastOne(ProgramError):
    def __init__(self) -> None:
        super().__init__(37, "Creators must be at least one if set")

    code = 37
    name = "CreatorsMustBeAtleastOne"
    msg = "Creators must be at least one if set"


class MustBeOneOfCreators(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            38, "If using a creators array, you must be one of the creators listed"
        )

    code = 38
    name = "MustBeOneOfCreators"
    msg = "If using a creators array, you must be one of the creators listed"


class NoCreatorsPresentOnMetadata(ProgramError):
    def __init__(self) -> None:
        super().__init__(39, "This metadata does not have creators")

    code = 39
    name = "NoCreatorsPresentOnMetadata"
    msg = "This metadata does not have creators"


class CreatorNotFound(ProgramError):
    def __init__(self) -> None:
        super().__init__(40, "This creator address was not found")

    code = 40
    name = "CreatorNotFound"
    msg = "This creator address was not found"


class InvalidBasisPoints(ProgramError):
    def __init__(self) -> None:
        super().__init__(41, "Basis points cannot be more than 10000")

    code = 41
    name = "InvalidBasisPoints"
    msg = "Basis points cannot be more than 10000"


class PrimarySaleCanOnlyBeFlippedToTrue(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            42, "Primary sale can only be flipped to true and is immutable"
        )

    code = 42
    name = "PrimarySaleCanOnlyBeFlippedToTrue"
    msg = "Primary sale can only be flipped to true and is immutable"


class OwnerMismatch(ProgramError):
    def __init__(self) -> None:
        super().__init__(43, "Owner does not match that on the account given")

    code = 43
    name = "OwnerMismatch"
    msg = "Owner does not match that on the account given"


class NoBalanceInAccountForAuthorization(ProgramError):
    def __init__(self) -> None:
        super().__init__(44, "This account has no tokens to be used for authorization")

    code = 44
    name = "NoBalanceInAccountForAuthorization"
    msg = "This account has no tokens to be used for authorization"


class ShareTotalMustBe100(ProgramError):
    def __init__(self) -> None:
        super().__init__(45, "Share total must equal 100 for creator array")

    code = 45
    name = "ShareTotalMustBe100"
    msg = "Share total must equal 100 for creator array"


class ReservationExists(ProgramError):
    def __init__(self) -> None:
        super().__init__(46, "This reservation list already exists!")

    code = 46
    name = "ReservationExists"
    msg = "This reservation list already exists!"


class ReservationDoesNotExist(ProgramError):
    def __init__(self) -> None:
        super().__init__(47, "This reservation list does not exist!")

    code = 47
    name = "ReservationDoesNotExist"
    msg = "This reservation list does not exist!"


class ReservationNotSet(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            48, "This reservation list exists but was never set with reservations"
        )

    code = 48
    name = "ReservationNotSet"
    msg = "This reservation list exists but was never set with reservations"


class ReservationAlreadyMade(ProgramError):
    def __init__(self) -> None:
        super().__init__(49, "This reservation list has already been set!")

    code = 49
    name = "ReservationAlreadyMade"
    msg = "This reservation list has already been set!"


class BeyondMaxAddressSize(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            50, "Provided more addresses than max allowed in single reservation"
        )

    code = 50
    name = "BeyondMaxAddressSize"
    msg = "Provided more addresses than max allowed in single reservation"


class NumericalOverflowError(ProgramError):
    def __init__(self) -> None:
        super().__init__(51, "NumericalOverflowError")

    code = 51
    name = "NumericalOverflowError"
    msg = "NumericalOverflowError"


class ReservationBreachesMaximumSupply(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            52,
            "This reservation would go beyond the maximum supply of the master edition!",
        )

    code = 52
    name = "ReservationBreachesMaximumSupply"
    msg = "This reservation would go beyond the maximum supply of the master edition!"


class AddressNotInReservation(ProgramError):
    def __init__(self) -> None:
        super().__init__(53, "Address not in reservation!")

    code = 53
    name = "AddressNotInReservation"
    msg = "Address not in reservation!"


class CannotVerifyAnotherCreator(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            54, "You cannot unilaterally verify another creator, they must sign"
        )

    code = 54
    name = "CannotVerifyAnotherCreator"
    msg = "You cannot unilaterally verify another creator, they must sign"


class CannotUnverifyAnotherCreator(ProgramError):
    def __init__(self) -> None:
        super().__init__(55, "You cannot unilaterally unverify another creator")

    code = 55
    name = "CannotUnverifyAnotherCreator"
    msg = "You cannot unilaterally unverify another creator"


class SpotMismatch(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            56,
            "In initial reservation setting, spots remaining should equal total spots",
        )

    code = 56
    name = "SpotMismatch"
    msg = "In initial reservation setting, spots remaining should equal total spots"


class IncorrectOwner(ProgramError):
    def __init__(self) -> None:
        super().__init__(57, "Incorrect account owner")

    code = 57
    name = "IncorrectOwner"
    msg = "Incorrect account owner"


class PrintingWouldBreachMaximumSupply(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            58,
            "printing these tokens would breach the maximum supply limit of the master edition",
        )

    code = 58
    name = "PrintingWouldBreachMaximumSupply"
    msg = "printing these tokens would breach the maximum supply limit of the master edition"


class DataIsImmutable(ProgramError):
    def __init__(self) -> None:
        super().__init__(59, "Data is immutable")

    code = 59
    name = "DataIsImmutable"
    msg = "Data is immutable"


class DuplicateCreatorAddress(ProgramError):
    def __init__(self) -> None:
        super().__init__(60, "No duplicate creator addresses")

    code = 60
    name = "DuplicateCreatorAddress"
    msg = "No duplicate creator addresses"


class ReservationSpotsRemainingShouldMatchTotalSpotsAtStart(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            61,
            "Reservation spots remaining should match total spots when first being created",
        )

    code = 61
    name = "ReservationSpotsRemainingShouldMatchTotalSpotsAtStart"
    msg = (
        "Reservation spots remaining should match total spots when first being created"
    )


class InvalidTokenProgram(ProgramError):
    def __init__(self) -> None:
        super().__init__(62, "Invalid token program")

    code = 62
    name = "InvalidTokenProgram"
    msg = "Invalid token program"


class DataTypeMismatch(ProgramError):
    def __init__(self) -> None:
        super().__init__(63, "Data type mismatch")

    code = 63
    name = "DataTypeMismatch"
    msg = "Data type mismatch"


class BeyondAlottedAddressSize(ProgramError):
    def __init__(self) -> None:
        super().__init__(64, "Beyond alotted address size in reservation!")

    code = 64
    name = "BeyondAlottedAddressSize"
    msg = "Beyond alotted address size in reservation!"


class ReservationNotComplete(ProgramError):
    def __init__(self) -> None:
        super().__init__(65, "The reservation has only been partially alotted")

    code = 65
    name = "ReservationNotComplete"
    msg = "The reservation has only been partially alotted"


class TriedToReplaceAnExistingReservation(ProgramError):
    def __init__(self) -> None:
        super().__init__(66, "You cannot splice over an existing reservation!")

    code = 66
    name = "TriedToReplaceAnExistingReservation"
    msg = "You cannot splice over an existing reservation!"


class InvalidOperation(ProgramError):
    def __init__(self) -> None:
        super().__init__(67, "Invalid operation")

    code = 67
    name = "InvalidOperation"
    msg = "Invalid operation"


class InvalidOwner(ProgramError):
    def __init__(self) -> None:
        super().__init__(68, "Invalid Owner")

    code = 68
    name = "InvalidOwner"
    msg = "Invalid Owner"


class PrintingMintSupplyMustBeZeroForConversion(ProgramError):
    def __init__(self) -> None:
        super().__init__(69, "Printing mint supply must be zero for conversion")

    code = 69
    name = "PrintingMintSupplyMustBeZeroForConversion"
    msg = "Printing mint supply must be zero for conversion"


class OneTimeAuthMintSupplyMustBeZeroForConversion(ProgramError):
    def __init__(self) -> None:
        super().__init__(70, "One Time Auth mint supply must be zero for conversion")

    code = 70
    name = "OneTimeAuthMintSupplyMustBeZeroForConversion"
    msg = "One Time Auth mint supply must be zero for conversion"


class InvalidEditionIndex(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            71, "You tried to insert one edition too many into an edition mark pda"
        )

    code = 71
    name = "InvalidEditionIndex"
    msg = "You tried to insert one edition too many into an edition mark pda"


class ReservationArrayShouldBeSizeOne(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            72,
            "In the legacy system the reservation needs to be of size one for cpu limit reasons",
        )

    code = 72
    name = "ReservationArrayShouldBeSizeOne"
    msg = "In the legacy system the reservation needs to be of size one for cpu limit reasons"


class isMutCanOnlyBeFlippedToFalse(ProgramError):
    def __init__(self) -> None:
        super().__init__(73, "Is Mutable can only be flipped to false")

    code = 73
    name = "isMutCanOnlyBeFlippedToFalse"
    msg = "Is Mutable can only be flipped to false"


class CollectionCannotBeVerifiedInThisInstruction(ProgramError):
    def __init__(self) -> None:
        super().__init__(74, "Cannont Verify Collection in this Instruction")

    code = 74
    name = "CollectionCannotBeVerifiedInThisInstruction"
    msg = "Cannont Verify Collection in this Instruction"


class Removed(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            75,
            "This instruction was deprecated in a previous release and is now removed",
        )

    code = 75
    name = "Removed"
    msg = "This instruction was deprecated in a previous release and is now removed"


class MustBeBurned(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            76,
            "This token use method is burn and there are no remaining uses, it must be burned",
        )

    code = 76
    name = "MustBeBurned"
    msg = "This token use method is burn and there are no remaining uses, it must be burned"


class InvalidUseMethod(ProgramError):
    def __init__(self) -> None:
        super().__init__(77, "This use method is invalid")

    code = 77
    name = "InvalidUseMethod"
    msg = "This use method is invalid"


class CannotChangeUseMethodAfterFirstUse(ProgramError):
    def __init__(self) -> None:
        super().__init__(78, "Cannot Change Use Method after the first use")

    code = 78
    name = "CannotChangeUseMethodAfterFirstUse"
    msg = "Cannot Change Use Method after the first use"


class CannotChangeUsesAfterFirstUse(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            79, "Cannot Change Remaining or Available uses after the first use"
        )

    code = 79
    name = "CannotChangeUsesAfterFirstUse"
    msg = "Cannot Change Remaining or Available uses after the first use"


class CollectionNotFound(ProgramError):
    def __init__(self) -> None:
        super().__init__(80, "Collection Not Found on Metadata")

    code = 80
    name = "CollectionNotFound"
    msg = "Collection Not Found on Metadata"


class InvalidCollectionUpdateAuthority(ProgramError):
    def __init__(self) -> None:
        super().__init__(81, "Collection Update Authority is invalid")

    code = 81
    name = "InvalidCollectionUpdateAuthority"
    msg = "Collection Update Authority is invalid"


class CollectionMustBeAUniqueMasterEdition(ProgramError):
    def __init__(self) -> None:
        super().__init__(82, "Collection Must Be a Unique Master Edition v2")

    code = 82
    name = "CollectionMustBeAUniqueMasterEdition"
    msg = "Collection Must Be a Unique Master Edition v2"


class UseAuthorityRecordAlreadyExists(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            83,
            "The Use Authority Record Already Exists, to modify it Revoke, then Approve",
        )

    code = 83
    name = "UseAuthorityRecordAlreadyExists"
    msg = "The Use Authority Record Already Exists, to modify it Revoke, then Approve"


class UseAuthorityRecordAlreadyRevoked(ProgramError):
    def __init__(self) -> None:
        super().__init__(84, "The Use Authority Record is empty or already revoked")

    code = 84
    name = "UseAuthorityRecordAlreadyRevoked"
    msg = "The Use Authority Record is empty or already revoked"


class Unusable(ProgramError):
    def __init__(self) -> None:
        super().__init__(85, "This token has no uses")

    code = 85
    name = "Unusable"
    msg = "This token has no uses"


class NotEnoughUses(ProgramError):
    def __init__(self) -> None:
        super().__init__(86, "There are not enough Uses left on this token.")

    code = 86
    name = "NotEnoughUses"
    msg = "There are not enough Uses left on this token."


class CollectionAuthorityRecordAlreadyExists(ProgramError):
    def __init__(self) -> None:
        super().__init__(87, "This Collection Authority Record Already Exists.")

    code = 87
    name = "CollectionAuthorityRecordAlreadyExists"
    msg = "This Collection Authority Record Already Exists."


class CollectionAuthorityDoesNotExist(ProgramError):
    def __init__(self) -> None:
        super().__init__(88, "This Collection Authority Record Does Not Exist.")

    code = 88
    name = "CollectionAuthorityDoesNotExist"
    msg = "This Collection Authority Record Does Not Exist."


class InvalidUseAuthorityRecord(ProgramError):
    def __init__(self) -> None:
        super().__init__(89, "This Use Authority Record is invalid.")

    code = 89
    name = "InvalidUseAuthorityRecord"
    msg = "This Use Authority Record is invalid."


class InvalidCollectionAuthorityRecord(ProgramError):
    def __init__(self) -> None:
        super().__init__(90, "This Collection Authority Record is invalid.")

    code = 90
    name = "InvalidCollectionAuthorityRecord"
    msg = "This Collection Authority Record is invalid."


class InvalidFreezeAuthority(ProgramError):
    def __init__(self) -> None:
        super().__init__(91, "Metadata does not match the freeze authority on the mint")

    code = 91
    name = "InvalidFreezeAuthority"
    msg = "Metadata does not match the freeze authority on the mint"


class InvalidDelegate(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            92, "All tokens in this account have not been delegated to this user."
        )

    code = 92
    name = "InvalidDelegate"
    msg = "All tokens in this account have not been delegated to this user."


class CannotAdjustVerifiedCreator(ProgramError):
    def __init__(self) -> None:
        super().__init__(93, "Creator can not be adjusted once they are verified.")

    code = 93
    name = "CannotAdjustVerifiedCreator"
    msg = "Creator can not be adjusted once they are verified."


class CannotRemoveVerifiedCreator(ProgramError):
    def __init__(self) -> None:
        super().__init__(94, "Verified creators cannot be removed.")

    code = 94
    name = "CannotRemoveVerifiedCreator"
    msg = "Verified creators cannot be removed."


class CannotWipeVerifiedCreators(ProgramError):
    def __init__(self) -> None:
        super().__init__(95, "Can not wipe verified creators.")

    code = 95
    name = "CannotWipeVerifiedCreators"
    msg = "Can not wipe verified creators."


class NotAllowedToChangeSellerFeeBasisPoints(ProgramError):
    def __init__(self) -> None:
        super().__init__(96, "Not allowed to change seller fee basis points.")

    code = 96
    name = "NotAllowedToChangeSellerFeeBasisPoints"
    msg = "Not allowed to change seller fee basis points."


class EditionOverrideCannotBeZero(ProgramError):
    def __init__(self) -> None:
        super().__init__(97, "Edition override cannot be zero")

    code = 97
    name = "EditionOverrideCannotBeZero"
    msg = "Edition override cannot be zero"


class InvalidUser(ProgramError):
    def __init__(self) -> None:
        super().__init__(98, "Invalid User")

    code = 98
    name = "InvalidUser"
    msg = "Invalid User"


CustomError = typing.Union[
    InstructionUnpackError,
    InstructionPackError,
    NotRentExempt,
    AlreadyInitialized,
    Uninitialized,
    InvalidMetadataKey,
    InvalidEditionKey,
    UpdateAuthorityIncorrect,
    UpdateAuthorityIsNotSigner,
    NotMintAuthority,
    InvalidMintAuthority,
    NameTooLong,
    SymbolTooLong,
    UriTooLong,
    UpdateAuthorityMustBeEqualToMetadataAuthorityAndSigner,
    MintMismatch,
    EditionsMustHaveExactlyOneToken,
    MaxEditionsMintedAlready,
    TokenMintToFailed,
    MasterRecordMismatch,
    DestinationMintMismatch,
    EditionAlreadyMinted,
    PrintingMintDecimalsShouldBeZero,
    OneTimePrintingAuthorizationMintDecimalsShouldBeZero,
    EditionMintDecimalsShouldBeZero,
    TokenBurnFailed,
    TokenAccountOneTimeAuthMintMismatch,
    DerivedKeyInvalid,
    PrintingMintMismatch,
    OneTimePrintingAuthMintMismatch,
    TokenAccountMintMismatch,
    TokenAccountMintMismatchV2,
    NotEnoughTokens,
    PrintingMintAuthorizationAccountMismatch,
    AuthorizationTokenAccountOwnerMismatch,
    Disabled,
    CreatorsTooLong,
    CreatorsMustBeAtleastOne,
    MustBeOneOfCreators,
    NoCreatorsPresentOnMetadata,
    CreatorNotFound,
    InvalidBasisPoints,
    PrimarySaleCanOnlyBeFlippedToTrue,
    OwnerMismatch,
    NoBalanceInAccountForAuthorization,
    ShareTotalMustBe100,
    ReservationExists,
    ReservationDoesNotExist,
    ReservationNotSet,
    ReservationAlreadyMade,
    BeyondMaxAddressSize,
    NumericalOverflowError,
    ReservationBreachesMaximumSupply,
    AddressNotInReservation,
    CannotVerifyAnotherCreator,
    CannotUnverifyAnotherCreator,
    SpotMismatch,
    IncorrectOwner,
    PrintingWouldBreachMaximumSupply,
    DataIsImmutable,
    DuplicateCreatorAddress,
    ReservationSpotsRemainingShouldMatchTotalSpotsAtStart,
    InvalidTokenProgram,
    DataTypeMismatch,
    BeyondAlottedAddressSize,
    ReservationNotComplete,
    TriedToReplaceAnExistingReservation,
    InvalidOperation,
    InvalidOwner,
    PrintingMintSupplyMustBeZeroForConversion,
    OneTimeAuthMintSupplyMustBeZeroForConversion,
    InvalidEditionIndex,
    ReservationArrayShouldBeSizeOne,
    isMutCanOnlyBeFlippedToFalse,
    CollectionCannotBeVerifiedInThisInstruction,
    Removed,
    MustBeBurned,
    InvalidUseMethod,
    CannotChangeUseMethodAfterFirstUse,
    CannotChangeUsesAfterFirstUse,
    CollectionNotFound,
    InvalidCollectionUpdateAuthority,
    CollectionMustBeAUniqueMasterEdition,
    UseAuthorityRecordAlreadyExists,
    UseAuthorityRecordAlreadyRevoked,
    Unusable,
    NotEnoughUses,
    CollectionAuthorityRecordAlreadyExists,
    CollectionAuthorityDoesNotExist,
    InvalidUseAuthorityRecord,
    InvalidCollectionAuthorityRecord,
    InvalidFreezeAuthority,
    InvalidDelegate,
    CannotAdjustVerifiedCreator,
    CannotRemoveVerifiedCreator,
    CannotWipeVerifiedCreators,
    NotAllowedToChangeSellerFeeBasisPoints,
    EditionOverrideCannotBeZero,
    InvalidUser,
]
CUSTOM_ERROR_MAP: dict[int, CustomError] = {
    0: InstructionUnpackError(),
    1: InstructionPackError(),
    2: NotRentExempt(),
    3: AlreadyInitialized(),
    4: Uninitialized(),
    5: InvalidMetadataKey(),
    6: InvalidEditionKey(),
    7: UpdateAuthorityIncorrect(),
    8: UpdateAuthorityIsNotSigner(),
    9: NotMintAuthority(),
    10: InvalidMintAuthority(),
    11: NameTooLong(),
    12: SymbolTooLong(),
    13: UriTooLong(),
    14: UpdateAuthorityMustBeEqualToMetadataAuthorityAndSigner(),
    15: MintMismatch(),
    16: EditionsMustHaveExactlyOneToken(),
    17: MaxEditionsMintedAlready(),
    18: TokenMintToFailed(),
    19: MasterRecordMismatch(),
    20: DestinationMintMismatch(),
    21: EditionAlreadyMinted(),
    22: PrintingMintDecimalsShouldBeZero(),
    23: OneTimePrintingAuthorizationMintDecimalsShouldBeZero(),
    24: EditionMintDecimalsShouldBeZero(),
    25: TokenBurnFailed(),
    26: TokenAccountOneTimeAuthMintMismatch(),
    27: DerivedKeyInvalid(),
    28: PrintingMintMismatch(),
    29: OneTimePrintingAuthMintMismatch(),
    30: TokenAccountMintMismatch(),
    31: TokenAccountMintMismatchV2(),
    32: NotEnoughTokens(),
    33: PrintingMintAuthorizationAccountMismatch(),
    34: AuthorizationTokenAccountOwnerMismatch(),
    35: Disabled(),
    36: CreatorsTooLong(),
    37: CreatorsMustBeAtleastOne(),
    38: MustBeOneOfCreators(),
    39: NoCreatorsPresentOnMetadata(),
    40: CreatorNotFound(),
    41: InvalidBasisPoints(),
    42: PrimarySaleCanOnlyBeFlippedToTrue(),
    43: OwnerMismatch(),
    44: NoBalanceInAccountForAuthorization(),
    45: ShareTotalMustBe100(),
    46: ReservationExists(),
    47: ReservationDoesNotExist(),
    48: ReservationNotSet(),
    49: ReservationAlreadyMade(),
    50: BeyondMaxAddressSize(),
    51: NumericalOverflowError(),
    52: ReservationBreachesMaximumSupply(),
    53: AddressNotInReservation(),
    54: CannotVerifyAnotherCreator(),
    55: CannotUnverifyAnotherCreator(),
    56: SpotMismatch(),
    57: IncorrectOwner(),
    58: PrintingWouldBreachMaximumSupply(),
    59: DataIsImmutable(),
    60: DuplicateCreatorAddress(),
    61: ReservationSpotsRemainingShouldMatchTotalSpotsAtStart(),
    62: InvalidTokenProgram(),
    63: DataTypeMismatch(),
    64: BeyondAlottedAddressSize(),
    65: ReservationNotComplete(),
    66: TriedToReplaceAnExistingReservation(),
    67: InvalidOperation(),
    68: InvalidOwner(),
    69: PrintingMintSupplyMustBeZeroForConversion(),
    70: OneTimeAuthMintSupplyMustBeZeroForConversion(),
    71: InvalidEditionIndex(),
    72: ReservationArrayShouldBeSizeOne(),
    73: isMutCanOnlyBeFlippedToFalse(),
    74: CollectionCannotBeVerifiedInThisInstruction(),
    75: Removed(),
    76: MustBeBurned(),
    77: InvalidUseMethod(),
    78: CannotChangeUseMethodAfterFirstUse(),
    79: CannotChangeUsesAfterFirstUse(),
    80: CollectionNotFound(),
    81: InvalidCollectionUpdateAuthority(),
    82: CollectionMustBeAUniqueMasterEdition(),
    83: UseAuthorityRecordAlreadyExists(),
    84: UseAuthorityRecordAlreadyRevoked(),
    85: Unusable(),
    86: NotEnoughUses(),
    87: CollectionAuthorityRecordAlreadyExists(),
    88: CollectionAuthorityDoesNotExist(),
    89: InvalidUseAuthorityRecord(),
    90: InvalidCollectionAuthorityRecord(),
    91: InvalidFreezeAuthority(),
    92: InvalidDelegate(),
    93: CannotAdjustVerifiedCreator(),
    94: CannotRemoveVerifiedCreator(),
    95: CannotWipeVerifiedCreators(),
    96: NotAllowedToChangeSellerFeeBasisPoints(),
    97: EditionOverrideCannotBeZero(),
    98: InvalidUser(),
}


def from_code(code: int) -> typing.Optional[CustomError]:
    maybe_err = CUSTOM_ERROR_MAP.get(code)
    if maybe_err is None:
        return None
    return maybe_err
