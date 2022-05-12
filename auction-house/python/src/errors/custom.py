import typing
from anchorpy.error import ProgramError


class PublicKeyMismatch(ProgramError):
    def __init__(self) -> None:
        super().__init__(6000, "PublicKeyMismatch")

    code = 6000
    name = "PublicKeyMismatch"
    msg = "PublicKeyMismatch"


class InvalidMintAuthority(ProgramError):
    def __init__(self) -> None:
        super().__init__(6001, "InvalidMintAuthority")

    code = 6001
    name = "InvalidMintAuthority"
    msg = "InvalidMintAuthority"


class UninitializedAccount(ProgramError):
    def __init__(self) -> None:
        super().__init__(6002, "UninitializedAccount")

    code = 6002
    name = "UninitializedAccount"
    msg = "UninitializedAccount"


class IncorrectOwner(ProgramError):
    def __init__(self) -> None:
        super().__init__(6003, "IncorrectOwner")

    code = 6003
    name = "IncorrectOwner"
    msg = "IncorrectOwner"


class PublicKeysShouldBeUnique(ProgramError):
    def __init__(self) -> None:
        super().__init__(6004, "PublicKeysShouldBeUnique")

    code = 6004
    name = "PublicKeysShouldBeUnique"
    msg = "PublicKeysShouldBeUnique"


class StatementFalse(ProgramError):
    def __init__(self) -> None:
        super().__init__(6005, "StatementFalse")

    code = 6005
    name = "StatementFalse"
    msg = "StatementFalse"


class NotRentExempt(ProgramError):
    def __init__(self) -> None:
        super().__init__(6006, "NotRentExempt")

    code = 6006
    name = "NotRentExempt"
    msg = "NotRentExempt"


class NumericalOverflow(ProgramError):
    def __init__(self) -> None:
        super().__init__(6007, "NumericalOverflow")

    code = 6007
    name = "NumericalOverflow"
    msg = "NumericalOverflow"


class ExpectedSolAccount(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6008, "Expected a sol account but got an spl token account instead"
        )

    code = 6008
    name = "ExpectedSolAccount"
    msg = "Expected a sol account but got an spl token account instead"


class CannotExchangeSOLForSol(ProgramError):
    def __init__(self) -> None:
        super().__init__(6009, "Cannot exchange sol for sol")

    code = 6009
    name = "CannotExchangeSOLForSol"
    msg = "Cannot exchange sol for sol"


class SOLWalletMustSign(ProgramError):
    def __init__(self) -> None:
        super().__init__(6010, "If paying with sol, sol wallet must be signer")

    code = 6010
    name = "SOLWalletMustSign"
    msg = "If paying with sol, sol wallet must be signer"


class CannotTakeThisActionWithoutAuctionHouseSignOff(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6011, "Cannot take this action without auction house signing too"
        )

    code = 6011
    name = "CannotTakeThisActionWithoutAuctionHouseSignOff"
    msg = "Cannot take this action without auction house signing too"


class NoPayerPresent(ProgramError):
    def __init__(self) -> None:
        super().__init__(6012, "No payer present on this txn")

    code = 6012
    name = "NoPayerPresent"
    msg = "No payer present on this txn"


class DerivedKeyInvalid(ProgramError):
    def __init__(self) -> None:
        super().__init__(6013, "Derived key invalid")

    code = 6013
    name = "DerivedKeyInvalid"
    msg = "Derived key invalid"


class MetadataDoesntExist(ProgramError):
    def __init__(self) -> None:
        super().__init__(6014, "Metadata doesn't exist")

    code = 6014
    name = "MetadataDoesntExist"
    msg = "Metadata doesn't exist"


class InvalidTokenAmount(ProgramError):
    def __init__(self) -> None:
        super().__init__(6015, "Invalid token amount")

    code = 6015
    name = "InvalidTokenAmount"
    msg = "Invalid token amount"


class BothPartiesNeedToAgreeToSale(ProgramError):
    def __init__(self) -> None:
        super().__init__(6016, "Both parties need to agree to this sale")

    code = 6016
    name = "BothPartiesNeedToAgreeToSale"
    msg = "Both parties need to agree to this sale"


class CannotMatchFreeSalesWithoutAuctionHouseOrSellerSignoff(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6017, "Cannot match free sales unless the auction house or seller signs off"
        )

    code = 6017
    name = "CannotMatchFreeSalesWithoutAuctionHouseOrSellerSignoff"
    msg = "Cannot match free sales unless the auction house or seller signs off"


class SaleRequiresSigner(ProgramError):
    def __init__(self) -> None:
        super().__init__(6018, "This sale requires a signer")

    code = 6018
    name = "SaleRequiresSigner"
    msg = "This sale requires a signer"


class OldSellerNotInitialized(ProgramError):
    def __init__(self) -> None:
        super().__init__(6019, "Old seller not initialized")

    code = 6019
    name = "OldSellerNotInitialized"
    msg = "Old seller not initialized"


class SellerATACannotHaveDelegate(ProgramError):
    def __init__(self) -> None:
        super().__init__(6020, "Seller ata cannot have a delegate set")

    code = 6020
    name = "SellerATACannotHaveDelegate"
    msg = "Seller ata cannot have a delegate set"


class BuyerATACannotHaveDelegate(ProgramError):
    def __init__(self) -> None:
        super().__init__(6021, "Buyer ata cannot have a delegate set")

    code = 6021
    name = "BuyerATACannotHaveDelegate"
    msg = "Buyer ata cannot have a delegate set"


class NoValidSignerPresent(ProgramError):
    def __init__(self) -> None:
        super().__init__(6022, "No valid signer present")

    code = 6022
    name = "NoValidSignerPresent"
    msg = "No valid signer present"


class InvalidBasisPoints(ProgramError):
    def __init__(self) -> None:
        super().__init__(6023, "BP must be less than or equal to 10000")

    code = 6023
    name = "InvalidBasisPoints"
    msg = "BP must be less than or equal to 10000"


class TradeStateDoesntExist(ProgramError):
    def __init__(self) -> None:
        super().__init__(6024, "The trade state account does not exist")

    code = 6024
    name = "TradeStateDoesntExist"
    msg = "The trade state account does not exist"


class TradeStateIsNotEmpty(ProgramError):
    def __init__(self) -> None:
        super().__init__(6025, "The trade state is not empty")

    code = 6025
    name = "TradeStateIsNotEmpty"
    msg = "The trade state is not empty"


class ReceiptIsEmpty(ProgramError):
    def __init__(self) -> None:
        super().__init__(6026, "The receipt is empty")

    code = 6026
    name = "ReceiptIsEmpty"
    msg = "The receipt is empty"


class InstructionMismatch(ProgramError):
    def __init__(self) -> None:
        super().__init__(6027, "The instruction does not match")

    code = 6027
    name = "InstructionMismatch"
    msg = "The instruction does not match"


class EscrowUnderRentExemption(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6028,
            "The instruction would drain the escrow below rent exemption threshold",
        )

    code = 6028
    name = "EscrowUnderRentExemption"
    msg = "The instruction would drain the escrow below rent exemption threshold"


CustomError = typing.Union[
    PublicKeyMismatch,
    InvalidMintAuthority,
    UninitializedAccount,
    IncorrectOwner,
    PublicKeysShouldBeUnique,
    StatementFalse,
    NotRentExempt,
    NumericalOverflow,
    ExpectedSolAccount,
    CannotExchangeSOLForSol,
    SOLWalletMustSign,
    CannotTakeThisActionWithoutAuctionHouseSignOff,
    NoPayerPresent,
    DerivedKeyInvalid,
    MetadataDoesntExist,
    InvalidTokenAmount,
    BothPartiesNeedToAgreeToSale,
    CannotMatchFreeSalesWithoutAuctionHouseOrSellerSignoff,
    SaleRequiresSigner,
    OldSellerNotInitialized,
    SellerATACannotHaveDelegate,
    BuyerATACannotHaveDelegate,
    NoValidSignerPresent,
    InvalidBasisPoints,
    TradeStateDoesntExist,
    TradeStateIsNotEmpty,
    ReceiptIsEmpty,
    InstructionMismatch,
    EscrowUnderRentExemption,
]
CUSTOM_ERROR_MAP: dict[int, CustomError] = {
    6000: PublicKeyMismatch(),
    6001: InvalidMintAuthority(),
    6002: UninitializedAccount(),
    6003: IncorrectOwner(),
    6004: PublicKeysShouldBeUnique(),
    6005: StatementFalse(),
    6006: NotRentExempt(),
    6007: NumericalOverflow(),
    6008: ExpectedSolAccount(),
    6009: CannotExchangeSOLForSol(),
    6010: SOLWalletMustSign(),
    6011: CannotTakeThisActionWithoutAuctionHouseSignOff(),
    6012: NoPayerPresent(),
    6013: DerivedKeyInvalid(),
    6014: MetadataDoesntExist(),
    6015: InvalidTokenAmount(),
    6016: BothPartiesNeedToAgreeToSale(),
    6017: CannotMatchFreeSalesWithoutAuctionHouseOrSellerSignoff(),
    6018: SaleRequiresSigner(),
    6019: OldSellerNotInitialized(),
    6020: SellerATACannotHaveDelegate(),
    6021: BuyerATACannotHaveDelegate(),
    6022: NoValidSignerPresent(),
    6023: InvalidBasisPoints(),
    6024: TradeStateDoesntExist(),
    6025: TradeStateIsNotEmpty(),
    6026: ReceiptIsEmpty(),
    6027: InstructionMismatch(),
    6028: EscrowUnderRentExemption(),
}


def from_code(code: int) -> typing.Optional[CustomError]:
    maybe_err = CUSTOM_ERROR_MAP.get(code)
    if maybe_err is None:
        return None
    return maybe_err
