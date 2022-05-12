from __future__ import annotations
import typing
from dataclasses import dataclass
from anchorpy.borsh_extension import EnumForCodegen
import borsh_construct as borsh


class IncorrectOwnerJSON(typing.TypedDict):
    kind: typing.Literal["IncorrectOwner"]


class UninitializedJSON(typing.TypedDict):
    kind: typing.Literal["Uninitialized"]


class MintMismatchJSON(typing.TypedDict):
    kind: typing.Literal["MintMismatch"]


class IndexGreaterThanLengthJSON(typing.TypedDict):
    kind: typing.Literal["IndexGreaterThanLength"]


class NumericalOverflowErrorJSON(typing.TypedDict):
    kind: typing.Literal["NumericalOverflowError"]


class TooManyCreatorsJSON(typing.TypedDict):
    kind: typing.Literal["TooManyCreators"]


class UuidMustBeExactly6LengthJSON(typing.TypedDict):
    kind: typing.Literal["UuidMustBeExactly6Length"]


class NotEnoughTokensJSON(typing.TypedDict):
    kind: typing.Literal["NotEnoughTokens"]


class NotEnoughSOLJSON(typing.TypedDict):
    kind: typing.Literal["NotEnoughSOL"]


class TokenTransferFailedJSON(typing.TypedDict):
    kind: typing.Literal["TokenTransferFailed"]


class CandyMachineEmptyJSON(typing.TypedDict):
    kind: typing.Literal["CandyMachineEmpty"]


class CandyMachineNotLiveJSON(typing.TypedDict):
    kind: typing.Literal["CandyMachineNotLive"]


class HiddenSettingsConfigsDoNotHaveConfigLinesJSON(typing.TypedDict):
    kind: typing.Literal["HiddenSettingsConfigsDoNotHaveConfigLines"]


class CannotChangeNumberOfLinesJSON(typing.TypedDict):
    kind: typing.Literal["CannotChangeNumberOfLines"]


class DerivedKeyInvalidJSON(typing.TypedDict):
    kind: typing.Literal["DerivedKeyInvalid"]


class PublicKeyMismatchJSON(typing.TypedDict):
    kind: typing.Literal["PublicKeyMismatch"]


class NoWhitelistTokenJSON(typing.TypedDict):
    kind: typing.Literal["NoWhitelistToken"]


class TokenBurnFailedJSON(typing.TypedDict):
    kind: typing.Literal["TokenBurnFailed"]


class GatewayAppMissingJSON(typing.TypedDict):
    kind: typing.Literal["GatewayAppMissing"]


class GatewayTokenMissingJSON(typing.TypedDict):
    kind: typing.Literal["GatewayTokenMissing"]


class GatewayTokenExpireTimeInvalidJSON(typing.TypedDict):
    kind: typing.Literal["GatewayTokenExpireTimeInvalid"]


class NetworkExpireFeatureMissingJSON(typing.TypedDict):
    kind: typing.Literal["NetworkExpireFeatureMissing"]


class CannotFindUsableConfigLineJSON(typing.TypedDict):
    kind: typing.Literal["CannotFindUsableConfigLine"]


class InvalidStringJSON(typing.TypedDict):
    kind: typing.Literal["InvalidString"]


class SuspiciousTransactionJSON(typing.TypedDict):
    kind: typing.Literal["SuspiciousTransaction"]


class CannotSwitchToHiddenSettingsJSON(typing.TypedDict):
    kind: typing.Literal["CannotSwitchToHiddenSettings"]


class IncorrectSlotHashesPubkeyJSON(typing.TypedDict):
    kind: typing.Literal["IncorrectSlotHashesPubkey"]


class IncorrectCollectionAuthorityJSON(typing.TypedDict):
    kind: typing.Literal["IncorrectCollectionAuthority"]


class MismatchedCollectionPDAJSON(typing.TypedDict):
    kind: typing.Literal["MismatchedCollectionPDA"]


class MismatchedCollectionMintJSON(typing.TypedDict):
    kind: typing.Literal["MismatchedCollectionMint"]


@dataclass
class IncorrectOwner:
    discriminator: typing.ClassVar = 0
    kind: typing.ClassVar = "IncorrectOwner"

    @classmethod
    def to_json(cls) -> IncorrectOwnerJSON:
        return IncorrectOwnerJSON(
            kind="IncorrectOwner",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "IncorrectOwner": {},
        }


@dataclass
class Uninitialized:
    discriminator: typing.ClassVar = 1
    kind: typing.ClassVar = "Uninitialized"

    @classmethod
    def to_json(cls) -> UninitializedJSON:
        return UninitializedJSON(
            kind="Uninitialized",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "Uninitialized": {},
        }


@dataclass
class MintMismatch:
    discriminator: typing.ClassVar = 2
    kind: typing.ClassVar = "MintMismatch"

    @classmethod
    def to_json(cls) -> MintMismatchJSON:
        return MintMismatchJSON(
            kind="MintMismatch",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "MintMismatch": {},
        }


@dataclass
class IndexGreaterThanLength:
    discriminator: typing.ClassVar = 3
    kind: typing.ClassVar = "IndexGreaterThanLength"

    @classmethod
    def to_json(cls) -> IndexGreaterThanLengthJSON:
        return IndexGreaterThanLengthJSON(
            kind="IndexGreaterThanLength",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "IndexGreaterThanLength": {},
        }


@dataclass
class NumericalOverflowError:
    discriminator: typing.ClassVar = 4
    kind: typing.ClassVar = "NumericalOverflowError"

    @classmethod
    def to_json(cls) -> NumericalOverflowErrorJSON:
        return NumericalOverflowErrorJSON(
            kind="NumericalOverflowError",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "NumericalOverflowError": {},
        }


@dataclass
class TooManyCreators:
    discriminator: typing.ClassVar = 5
    kind: typing.ClassVar = "TooManyCreators"

    @classmethod
    def to_json(cls) -> TooManyCreatorsJSON:
        return TooManyCreatorsJSON(
            kind="TooManyCreators",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "TooManyCreators": {},
        }


@dataclass
class UuidMustBeExactly6Length:
    discriminator: typing.ClassVar = 6
    kind: typing.ClassVar = "UuidMustBeExactly6Length"

    @classmethod
    def to_json(cls) -> UuidMustBeExactly6LengthJSON:
        return UuidMustBeExactly6LengthJSON(
            kind="UuidMustBeExactly6Length",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "UuidMustBeExactly6Length": {},
        }


@dataclass
class NotEnoughTokens:
    discriminator: typing.ClassVar = 7
    kind: typing.ClassVar = "NotEnoughTokens"

    @classmethod
    def to_json(cls) -> NotEnoughTokensJSON:
        return NotEnoughTokensJSON(
            kind="NotEnoughTokens",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "NotEnoughTokens": {},
        }


@dataclass
class NotEnoughSOL:
    discriminator: typing.ClassVar = 8
    kind: typing.ClassVar = "NotEnoughSOL"

    @classmethod
    def to_json(cls) -> NotEnoughSOLJSON:
        return NotEnoughSOLJSON(
            kind="NotEnoughSOL",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "NotEnoughSOL": {},
        }


@dataclass
class TokenTransferFailed:
    discriminator: typing.ClassVar = 9
    kind: typing.ClassVar = "TokenTransferFailed"

    @classmethod
    def to_json(cls) -> TokenTransferFailedJSON:
        return TokenTransferFailedJSON(
            kind="TokenTransferFailed",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "TokenTransferFailed": {},
        }


@dataclass
class CandyMachineEmpty:
    discriminator: typing.ClassVar = 10
    kind: typing.ClassVar = "CandyMachineEmpty"

    @classmethod
    def to_json(cls) -> CandyMachineEmptyJSON:
        return CandyMachineEmptyJSON(
            kind="CandyMachineEmpty",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "CandyMachineEmpty": {},
        }


@dataclass
class CandyMachineNotLive:
    discriminator: typing.ClassVar = 11
    kind: typing.ClassVar = "CandyMachineNotLive"

    @classmethod
    def to_json(cls) -> CandyMachineNotLiveJSON:
        return CandyMachineNotLiveJSON(
            kind="CandyMachineNotLive",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "CandyMachineNotLive": {},
        }


@dataclass
class HiddenSettingsConfigsDoNotHaveConfigLines:
    discriminator: typing.ClassVar = 12
    kind: typing.ClassVar = "HiddenSettingsConfigsDoNotHaveConfigLines"

    @classmethod
    def to_json(cls) -> HiddenSettingsConfigsDoNotHaveConfigLinesJSON:
        return HiddenSettingsConfigsDoNotHaveConfigLinesJSON(
            kind="HiddenSettingsConfigsDoNotHaveConfigLines",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "HiddenSettingsConfigsDoNotHaveConfigLines": {},
        }


@dataclass
class CannotChangeNumberOfLines:
    discriminator: typing.ClassVar = 13
    kind: typing.ClassVar = "CannotChangeNumberOfLines"

    @classmethod
    def to_json(cls) -> CannotChangeNumberOfLinesJSON:
        return CannotChangeNumberOfLinesJSON(
            kind="CannotChangeNumberOfLines",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "CannotChangeNumberOfLines": {},
        }


@dataclass
class DerivedKeyInvalid:
    discriminator: typing.ClassVar = 14
    kind: typing.ClassVar = "DerivedKeyInvalid"

    @classmethod
    def to_json(cls) -> DerivedKeyInvalidJSON:
        return DerivedKeyInvalidJSON(
            kind="DerivedKeyInvalid",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "DerivedKeyInvalid": {},
        }


@dataclass
class PublicKeyMismatch:
    discriminator: typing.ClassVar = 15
    kind: typing.ClassVar = "PublicKeyMismatch"

    @classmethod
    def to_json(cls) -> PublicKeyMismatchJSON:
        return PublicKeyMismatchJSON(
            kind="PublicKeyMismatch",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "PublicKeyMismatch": {},
        }


@dataclass
class NoWhitelistToken:
    discriminator: typing.ClassVar = 16
    kind: typing.ClassVar = "NoWhitelistToken"

    @classmethod
    def to_json(cls) -> NoWhitelistTokenJSON:
        return NoWhitelistTokenJSON(
            kind="NoWhitelistToken",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "NoWhitelistToken": {},
        }


@dataclass
class TokenBurnFailed:
    discriminator: typing.ClassVar = 17
    kind: typing.ClassVar = "TokenBurnFailed"

    @classmethod
    def to_json(cls) -> TokenBurnFailedJSON:
        return TokenBurnFailedJSON(
            kind="TokenBurnFailed",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "TokenBurnFailed": {},
        }


@dataclass
class GatewayAppMissing:
    discriminator: typing.ClassVar = 18
    kind: typing.ClassVar = "GatewayAppMissing"

    @classmethod
    def to_json(cls) -> GatewayAppMissingJSON:
        return GatewayAppMissingJSON(
            kind="GatewayAppMissing",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "GatewayAppMissing": {},
        }


@dataclass
class GatewayTokenMissing:
    discriminator: typing.ClassVar = 19
    kind: typing.ClassVar = "GatewayTokenMissing"

    @classmethod
    def to_json(cls) -> GatewayTokenMissingJSON:
        return GatewayTokenMissingJSON(
            kind="GatewayTokenMissing",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "GatewayTokenMissing": {},
        }


@dataclass
class GatewayTokenExpireTimeInvalid:
    discriminator: typing.ClassVar = 20
    kind: typing.ClassVar = "GatewayTokenExpireTimeInvalid"

    @classmethod
    def to_json(cls) -> GatewayTokenExpireTimeInvalidJSON:
        return GatewayTokenExpireTimeInvalidJSON(
            kind="GatewayTokenExpireTimeInvalid",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "GatewayTokenExpireTimeInvalid": {},
        }


@dataclass
class NetworkExpireFeatureMissing:
    discriminator: typing.ClassVar = 21
    kind: typing.ClassVar = "NetworkExpireFeatureMissing"

    @classmethod
    def to_json(cls) -> NetworkExpireFeatureMissingJSON:
        return NetworkExpireFeatureMissingJSON(
            kind="NetworkExpireFeatureMissing",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "NetworkExpireFeatureMissing": {},
        }


@dataclass
class CannotFindUsableConfigLine:
    discriminator: typing.ClassVar = 22
    kind: typing.ClassVar = "CannotFindUsableConfigLine"

    @classmethod
    def to_json(cls) -> CannotFindUsableConfigLineJSON:
        return CannotFindUsableConfigLineJSON(
            kind="CannotFindUsableConfigLine",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "CannotFindUsableConfigLine": {},
        }


@dataclass
class InvalidString:
    discriminator: typing.ClassVar = 23
    kind: typing.ClassVar = "InvalidString"

    @classmethod
    def to_json(cls) -> InvalidStringJSON:
        return InvalidStringJSON(
            kind="InvalidString",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "InvalidString": {},
        }


@dataclass
class SuspiciousTransaction:
    discriminator: typing.ClassVar = 24
    kind: typing.ClassVar = "SuspiciousTransaction"

    @classmethod
    def to_json(cls) -> SuspiciousTransactionJSON:
        return SuspiciousTransactionJSON(
            kind="SuspiciousTransaction",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "SuspiciousTransaction": {},
        }


@dataclass
class CannotSwitchToHiddenSettings:
    discriminator: typing.ClassVar = 25
    kind: typing.ClassVar = "CannotSwitchToHiddenSettings"

    @classmethod
    def to_json(cls) -> CannotSwitchToHiddenSettingsJSON:
        return CannotSwitchToHiddenSettingsJSON(
            kind="CannotSwitchToHiddenSettings",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "CannotSwitchToHiddenSettings": {},
        }


@dataclass
class IncorrectSlotHashesPubkey:
    discriminator: typing.ClassVar = 26
    kind: typing.ClassVar = "IncorrectSlotHashesPubkey"

    @classmethod
    def to_json(cls) -> IncorrectSlotHashesPubkeyJSON:
        return IncorrectSlotHashesPubkeyJSON(
            kind="IncorrectSlotHashesPubkey",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "IncorrectSlotHashesPubkey": {},
        }


@dataclass
class IncorrectCollectionAuthority:
    discriminator: typing.ClassVar = 27
    kind: typing.ClassVar = "IncorrectCollectionAuthority"

    @classmethod
    def to_json(cls) -> IncorrectCollectionAuthorityJSON:
        return IncorrectCollectionAuthorityJSON(
            kind="IncorrectCollectionAuthority",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "IncorrectCollectionAuthority": {},
        }


@dataclass
class MismatchedCollectionPDA:
    discriminator: typing.ClassVar = 28
    kind: typing.ClassVar = "MismatchedCollectionPDA"

    @classmethod
    def to_json(cls) -> MismatchedCollectionPDAJSON:
        return MismatchedCollectionPDAJSON(
            kind="MismatchedCollectionPDA",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "MismatchedCollectionPDA": {},
        }


@dataclass
class MismatchedCollectionMint:
    discriminator: typing.ClassVar = 29
    kind: typing.ClassVar = "MismatchedCollectionMint"

    @classmethod
    def to_json(cls) -> MismatchedCollectionMintJSON:
        return MismatchedCollectionMintJSON(
            kind="MismatchedCollectionMint",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "MismatchedCollectionMint": {},
        }


ErrorCodeKind = typing.Union[
    IncorrectOwner,
    Uninitialized,
    MintMismatch,
    IndexGreaterThanLength,
    NumericalOverflowError,
    TooManyCreators,
    UuidMustBeExactly6Length,
    NotEnoughTokens,
    NotEnoughSOL,
    TokenTransferFailed,
    CandyMachineEmpty,
    CandyMachineNotLive,
    HiddenSettingsConfigsDoNotHaveConfigLines,
    CannotChangeNumberOfLines,
    DerivedKeyInvalid,
    PublicKeyMismatch,
    NoWhitelistToken,
    TokenBurnFailed,
    GatewayAppMissing,
    GatewayTokenMissing,
    GatewayTokenExpireTimeInvalid,
    NetworkExpireFeatureMissing,
    CannotFindUsableConfigLine,
    InvalidString,
    SuspiciousTransaction,
    CannotSwitchToHiddenSettings,
    IncorrectSlotHashesPubkey,
    IncorrectCollectionAuthority,
    MismatchedCollectionPDA,
    MismatchedCollectionMint,
]
ErrorCodeJSON = typing.Union[
    IncorrectOwnerJSON,
    UninitializedJSON,
    MintMismatchJSON,
    IndexGreaterThanLengthJSON,
    NumericalOverflowErrorJSON,
    TooManyCreatorsJSON,
    UuidMustBeExactly6LengthJSON,
    NotEnoughTokensJSON,
    NotEnoughSOLJSON,
    TokenTransferFailedJSON,
    CandyMachineEmptyJSON,
    CandyMachineNotLiveJSON,
    HiddenSettingsConfigsDoNotHaveConfigLinesJSON,
    CannotChangeNumberOfLinesJSON,
    DerivedKeyInvalidJSON,
    PublicKeyMismatchJSON,
    NoWhitelistTokenJSON,
    TokenBurnFailedJSON,
    GatewayAppMissingJSON,
    GatewayTokenMissingJSON,
    GatewayTokenExpireTimeInvalidJSON,
    NetworkExpireFeatureMissingJSON,
    CannotFindUsableConfigLineJSON,
    InvalidStringJSON,
    SuspiciousTransactionJSON,
    CannotSwitchToHiddenSettingsJSON,
    IncorrectSlotHashesPubkeyJSON,
    IncorrectCollectionAuthorityJSON,
    MismatchedCollectionPDAJSON,
    MismatchedCollectionMintJSON,
]


def from_decoded(obj: dict) -> ErrorCodeKind:
    if not isinstance(obj, dict):
        raise ValueError("Invalid enum object")
    if "IncorrectOwner" in obj:
        return IncorrectOwner()
    if "Uninitialized" in obj:
        return Uninitialized()
    if "MintMismatch" in obj:
        return MintMismatch()
    if "IndexGreaterThanLength" in obj:
        return IndexGreaterThanLength()
    if "NumericalOverflowError" in obj:
        return NumericalOverflowError()
    if "TooManyCreators" in obj:
        return TooManyCreators()
    if "UuidMustBeExactly6Length" in obj:
        return UuidMustBeExactly6Length()
    if "NotEnoughTokens" in obj:
        return NotEnoughTokens()
    if "NotEnoughSOL" in obj:
        return NotEnoughSOL()
    if "TokenTransferFailed" in obj:
        return TokenTransferFailed()
    if "CandyMachineEmpty" in obj:
        return CandyMachineEmpty()
    if "CandyMachineNotLive" in obj:
        return CandyMachineNotLive()
    if "HiddenSettingsConfigsDoNotHaveConfigLines" in obj:
        return HiddenSettingsConfigsDoNotHaveConfigLines()
    if "CannotChangeNumberOfLines" in obj:
        return CannotChangeNumberOfLines()
    if "DerivedKeyInvalid" in obj:
        return DerivedKeyInvalid()
    if "PublicKeyMismatch" in obj:
        return PublicKeyMismatch()
    if "NoWhitelistToken" in obj:
        return NoWhitelistToken()
    if "TokenBurnFailed" in obj:
        return TokenBurnFailed()
    if "GatewayAppMissing" in obj:
        return GatewayAppMissing()
    if "GatewayTokenMissing" in obj:
        return GatewayTokenMissing()
    if "GatewayTokenExpireTimeInvalid" in obj:
        return GatewayTokenExpireTimeInvalid()
    if "NetworkExpireFeatureMissing" in obj:
        return NetworkExpireFeatureMissing()
    if "CannotFindUsableConfigLine" in obj:
        return CannotFindUsableConfigLine()
    if "InvalidString" in obj:
        return InvalidString()
    if "SuspiciousTransaction" in obj:
        return SuspiciousTransaction()
    if "CannotSwitchToHiddenSettings" in obj:
        return CannotSwitchToHiddenSettings()
    if "IncorrectSlotHashesPubkey" in obj:
        return IncorrectSlotHashesPubkey()
    if "IncorrectCollectionAuthority" in obj:
        return IncorrectCollectionAuthority()
    if "MismatchedCollectionPDA" in obj:
        return MismatchedCollectionPDA()
    if "MismatchedCollectionMint" in obj:
        return MismatchedCollectionMint()
    raise ValueError("Invalid enum object")


def from_json(obj: ErrorCodeJSON) -> ErrorCodeKind:
    if obj["kind"] == "IncorrectOwner":
        return IncorrectOwner()
    if obj["kind"] == "Uninitialized":
        return Uninitialized()
    if obj["kind"] == "MintMismatch":
        return MintMismatch()
    if obj["kind"] == "IndexGreaterThanLength":
        return IndexGreaterThanLength()
    if obj["kind"] == "NumericalOverflowError":
        return NumericalOverflowError()
    if obj["kind"] == "TooManyCreators":
        return TooManyCreators()
    if obj["kind"] == "UuidMustBeExactly6Length":
        return UuidMustBeExactly6Length()
    if obj["kind"] == "NotEnoughTokens":
        return NotEnoughTokens()
    if obj["kind"] == "NotEnoughSOL":
        return NotEnoughSOL()
    if obj["kind"] == "TokenTransferFailed":
        return TokenTransferFailed()
    if obj["kind"] == "CandyMachineEmpty":
        return CandyMachineEmpty()
    if obj["kind"] == "CandyMachineNotLive":
        return CandyMachineNotLive()
    if obj["kind"] == "HiddenSettingsConfigsDoNotHaveConfigLines":
        return HiddenSettingsConfigsDoNotHaveConfigLines()
    if obj["kind"] == "CannotChangeNumberOfLines":
        return CannotChangeNumberOfLines()
    if obj["kind"] == "DerivedKeyInvalid":
        return DerivedKeyInvalid()
    if obj["kind"] == "PublicKeyMismatch":
        return PublicKeyMismatch()
    if obj["kind"] == "NoWhitelistToken":
        return NoWhitelistToken()
    if obj["kind"] == "TokenBurnFailed":
        return TokenBurnFailed()
    if obj["kind"] == "GatewayAppMissing":
        return GatewayAppMissing()
    if obj["kind"] == "GatewayTokenMissing":
        return GatewayTokenMissing()
    if obj["kind"] == "GatewayTokenExpireTimeInvalid":
        return GatewayTokenExpireTimeInvalid()
    if obj["kind"] == "NetworkExpireFeatureMissing":
        return NetworkExpireFeatureMissing()
    if obj["kind"] == "CannotFindUsableConfigLine":
        return CannotFindUsableConfigLine()
    if obj["kind"] == "InvalidString":
        return InvalidString()
    if obj["kind"] == "SuspiciousTransaction":
        return SuspiciousTransaction()
    if obj["kind"] == "CannotSwitchToHiddenSettings":
        return CannotSwitchToHiddenSettings()
    if obj["kind"] == "IncorrectSlotHashesPubkey":
        return IncorrectSlotHashesPubkey()
    if obj["kind"] == "IncorrectCollectionAuthority":
        return IncorrectCollectionAuthority()
    if obj["kind"] == "MismatchedCollectionPDA":
        return MismatchedCollectionPDA()
    if obj["kind"] == "MismatchedCollectionMint":
        return MismatchedCollectionMint()
    kind = obj["kind"]
    raise ValueError(f"Unrecognized enum kind: {kind}")


layout = EnumForCodegen(
    "IncorrectOwner" / borsh.CStruct(),
    "Uninitialized" / borsh.CStruct(),
    "MintMismatch" / borsh.CStruct(),
    "IndexGreaterThanLength" / borsh.CStruct(),
    "NumericalOverflowError" / borsh.CStruct(),
    "TooManyCreators" / borsh.CStruct(),
    "UuidMustBeExactly6Length" / borsh.CStruct(),
    "NotEnoughTokens" / borsh.CStruct(),
    "NotEnoughSOL" / borsh.CStruct(),
    "TokenTransferFailed" / borsh.CStruct(),
    "CandyMachineEmpty" / borsh.CStruct(),
    "CandyMachineNotLive" / borsh.CStruct(),
    "HiddenSettingsConfigsDoNotHaveConfigLines" / borsh.CStruct(),
    "CannotChangeNumberOfLines" / borsh.CStruct(),
    "DerivedKeyInvalid" / borsh.CStruct(),
    "PublicKeyMismatch" / borsh.CStruct(),
    "NoWhitelistToken" / borsh.CStruct(),
    "TokenBurnFailed" / borsh.CStruct(),
    "GatewayAppMissing" / borsh.CStruct(),
    "GatewayTokenMissing" / borsh.CStruct(),
    "GatewayTokenExpireTimeInvalid" / borsh.CStruct(),
    "NetworkExpireFeatureMissing" / borsh.CStruct(),
    "CannotFindUsableConfigLine" / borsh.CStruct(),
    "InvalidString" / borsh.CStruct(),
    "SuspiciousTransaction" / borsh.CStruct(),
    "CannotSwitchToHiddenSettings" / borsh.CStruct(),
    "IncorrectSlotHashesPubkey" / borsh.CStruct(),
    "IncorrectCollectionAuthority" / borsh.CStruct(),
    "MismatchedCollectionPDA" / borsh.CStruct(),
    "MismatchedCollectionMint" / borsh.CStruct(),
)
