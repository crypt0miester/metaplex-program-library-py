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


class DerivedKeyInvalid(ProgramError):
    def __init__(self) -> None:
        super().__init__(6008, "Derived key invalid")

    code = 6008
    name = "DerivedKeyInvalid"
    msg = "Derived key invalid"


class MetadataDoesntExist(ProgramError):
    def __init__(self) -> None:
        super().__init__(6009, "Metadata doesn't exist")

    code = 6009
    name = "MetadataDoesntExist"
    msg = "Metadata doesn't exist"


class EditionDoesntExist(ProgramError):
    def __init__(self) -> None:
        super().__init__(6010, "Edition doesn't exist")

    code = 6010
    name = "EditionDoesntExist"
    msg = "Edition doesn't exist"


class InvalidTokenAmount(ProgramError):
    def __init__(self) -> None:
        super().__init__(6011, "Invalid token amount")

    code = 6011
    name = "InvalidTokenAmount"
    msg = "Invalid token amount"


class InvalidMint(ProgramError):
    def __init__(self) -> None:
        super().__init__(6012, "This token is not a valid mint for this entangled pair")

    code = 6012
    name = "InvalidMint"
    msg = "This token is not a valid mint for this entangled pair"


class EntangledPairExists(ProgramError):
    def __init__(self) -> None:
        super().__init__(6013, "This pair already exists as it's reverse")

    code = 6013
    name = "EntangledPairExists"
    msg = "This pair already exists as it's reverse"


class MustHaveSupplyOne(ProgramError):
    def __init__(self) -> None:
        super().__init__(6014, "Must have supply one!")

    code = 6014
    name = "MustHaveSupplyOne"
    msg = "Must have supply one!"


CustomError = typing.Union[
    PublicKeyMismatch,
    InvalidMintAuthority,
    UninitializedAccount,
    IncorrectOwner,
    PublicKeysShouldBeUnique,
    StatementFalse,
    NotRentExempt,
    NumericalOverflow,
    DerivedKeyInvalid,
    MetadataDoesntExist,
    EditionDoesntExist,
    InvalidTokenAmount,
    InvalidMint,
    EntangledPairExists,
    MustHaveSupplyOne,
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
    6008: DerivedKeyInvalid(),
    6009: MetadataDoesntExist(),
    6010: EditionDoesntExist(),
    6011: InvalidTokenAmount(),
    6012: InvalidMint(),
    6013: EntangledPairExists(),
    6014: MustHaveSupplyOne(),
}


def from_code(code: int) -> typing.Optional[CustomError]:
    maybe_err = CUSTOM_ERROR_MAP.get(code)
    if maybe_err is None:
        return None
    return maybe_err
