from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from generated.types.pkg_2021.pkg_10.pkg_01.pkg_0001.gtw_types import (
    File50MbhashType,
    FileUnlimitedHashType,
)

__NAMESPACE__ = (
    "http://ksef.mf.gov.pl/schema/gtw/svc/batch/types/2021/10/01/0001"
)


class CompressionTypeType(Enum):
    ZIP = "zip"


class PackageTypeType(Enum):
    SINGLE = "single"
    SPLIT = "split"


@dataclass
class PackageFileHashType(FileUnlimitedHashType):
    pass


@dataclass
class PackageType:
    package_type: Optional[PackageTypeType] = field(
        default=None,
        metadata={
            "name": "PackageType",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/batch/types/2021/10/01/0001",
            "required": True,
        },
    )
    compression_type: Optional[CompressionTypeType] = field(
        default=None,
        metadata={
            "name": "CompressionType",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/batch/types/2021/10/01/0001",
            "required": True,
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/batch/types/2021/10/01/0001",
            "required": True,
            "pattern": r"[a-zA-Z0-9_\.\-]{5,100}",
        },
    )


@dataclass
class PartFileHashType(File50MbhashType):
    pass


@dataclass
class PackagePartSignatureInitRequestType:
    """
    Package part bytes encrypted with service certificate public key
    (transformation AES/CBC/PKCS#7)
    """

    ordinal_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "OrdinalNumber",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/batch/types/2021/10/01/0001",
            "required": True,
            "min_exclusive": 0,
        },
    )
    part_file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartFileName",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/batch/types/2021/10/01/0001",
            "required": True,
            "pattern": r"[a-zA-Z0-9_\.\-]{5,100}",
        },
    )
    part_file_hash: Optional[PartFileHashType] = field(
        default=None,
        metadata={
            "name": "PartFileHash",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/batch/types/2021/10/01/0001",
            "required": True,
        },
    )
