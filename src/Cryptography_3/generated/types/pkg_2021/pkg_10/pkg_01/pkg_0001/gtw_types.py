from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001"


@dataclass
class AccountNumberType:
    nrb: Optional[str] = field(
        default=None,
        metadata={
            "name": "NRB",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "pattern": r"(PL)?[0-9]{2}[0-9]{8}[0-9]{16}",
        },
    )
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "pattern": r"[A-Z]{2}[0-9]{2}[A-Z0-9]{10,30}",
        },
    )


class AuthorisationTypeType(Enum):
    SERIAL_NUMBER = "SerialNumber"
    FINGERPRINT = "Fingerprint"


@dataclass
class EncryptionAlgorithmDataType:
    algorithm: str = field(
        init=False,
        default="AES",
        metadata={
            "name": "Algorithm",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )
    mode: str = field(
        init=False,
        default="CBC",
        metadata={
            "name": "Mode",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )
    padding: str = field(
        init=False,
        default="PKCS#7",
        metadata={
            "name": "Padding",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )


@dataclass
class EncryptionAlgorithmKeyType:
    algorithm: str = field(
        init=False,
        default="RSA",
        metadata={
            "name": "Algorithm",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )
    mode: str = field(
        init=False,
        default="ECB",
        metadata={
            "name": "Mode",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )
    padding: str = field(
        init=False,
        default="PKCS#1",
        metadata={
            "name": "Padding",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )


@dataclass
class EncryptionInitializationVectorType:
    encoding: str = field(
        init=False,
        default="Base64",
        metadata={
            "name": "Encoding",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )
    bytes: int = field(
        init=False,
        default=16,
        metadata={
            "name": "Bytes",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
            "min_length": 24,
            "max_length": 24,
        },
    )


@dataclass
class EncryptionKeyType:
    """
    :ivar encoding:
    :ivar algorithm:
    :ivar size:
    :ivar value: Encryption key bytes encrypted with service certificate
        public key (transformation RSA/ECB/PKCS#1) and then encoded with
        Base64
    """

    encoding: str = field(
        init=False,
        default="Base64",
        metadata={
            "name": "Encoding",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )
    algorithm: str = field(
        init=False,
        default="AES",
        metadata={
            "name": "Algorithm",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )
    size: int = field(
        init=False,
        default=256,
        metadata={
            "name": "Size",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
            "min_length": 344,
            "max_length": 344,
        },
    )


@dataclass
class FormCodeType:
    system_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SystemCode",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
            "min_length": 1,
            "max_length": 32,
        },
    )
    schema_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchemaVersion",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )
    target_namespace: Optional[str] = field(
        default=None,
        metadata={
            "name": "TargetNamespace",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class HashShatype:
    class Meta:
        name = "HashSHAType"

    algorithm: str = field(
        init=False,
        default="SHA-256",
        metadata={
            "name": "Algorithm",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )
    encoding: str = field(
        init=False,
        default="Base64",
        metadata={
            "name": "Encoding",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
            "min_length": 44,
            "max_length": 44,
        },
    )


class ServiceType(Enum):
    KSE_F = "KSeF"


@dataclass
class SubjectIdentifierByType:
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )


@dataclass
class SubjectIdentifierToType:
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )


@dataclass
class SubjectNameType:
    trade_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradeName",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class DocumentTypeType:
    service: Optional[ServiceType] = field(
        default=None,
        metadata={
            "name": "Service",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )
    form_code: Optional[FormCodeType] = field(
        default=None,
        metadata={
            "name": "FormCode",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )


@dataclass
class EncryptionType:
    encryption_key: Optional[EncryptionKeyType] = field(
        default=None,
        metadata={
            "name": "EncryptionKey",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )
    encryption_initialization_vector: Optional[
        EncryptionInitializationVectorType
    ] = field(
        default=None,
        metadata={
            "name": "EncryptionInitializationVector",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )
    encryption_algorithm_key: Optional[EncryptionAlgorithmKeyType] = field(
        default=None,
        metadata={
            "name": "EncryptionAlgorithmKey",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )
    encryption_algorithm_data: Optional[EncryptionAlgorithmDataType] = field(
        default=None,
        metadata={
            "name": "EncryptionAlgorithmData",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )


@dataclass
class File50MbhashType:
    class Meta:
        name = "File50MBHashType"

    hash_sha: Optional[HashShatype] = field(
        default=None,
        metadata={
            "name": "HashSHA",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )
    file_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "FileSize",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
            "min_exclusive": 0,
            "max_inclusive": 52428800,
        },
    )


@dataclass
class FileUnlimitedHashType:
    hash_sha: Optional[HashShatype] = field(
        default=None,
        metadata={
            "name": "HashSHA",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )
    file_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "FileSize",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
            "min_exclusive": 0,
        },
    )


@dataclass
class SubjectFullNameType(SubjectNameType):
    full_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FullName",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class SubjectIdentifierByCompanyType(SubjectIdentifierByType):
    pass


@dataclass
class SubjectIdentifierInternalType(SubjectIdentifierByType):
    pass


@dataclass
class SubjectIdentifierToCompanyType(SubjectIdentifierToType):
    pass


@dataclass
class SubjectIdentifierToNoneType(SubjectIdentifierToType):
    pass


@dataclass
class SubjectIdentifierToOtherTaxType(SubjectIdentifierToType):
    pass


@dataclass
class SubjectPersonNameType(SubjectNameType):
    first_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FirstName",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
            "min_length": 1,
            "max_length": 30,
        },
    )
    surname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
            "min_length": 1,
            "max_length": 81,
        },
    )
