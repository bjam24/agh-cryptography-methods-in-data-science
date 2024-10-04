from dataclasses import dataclass, field
from typing import List, Optional

from generated.batch.types.pkg_2021.pkg_10.pkg_01.pkg_0001.batch_types import (
    PackageFileHashType,
    PackagePartSignatureInitRequestType,
    PackageType,
)
from generated.types.pkg_2021.pkg_10.pkg_01.pkg_0001.gtw_types import (
    DocumentTypeType,
    EncryptionType,
    SubjectIdentifierByType,
)

__NAMESPACE__ = (
    "http://ksef.mf.gov.pl/schema/gtw/svc/batch/init/request/2021/10/01/0001"
)


@dataclass
class PackageSignatureInitRequestType:
    package: Optional[PackageType] = field(
        default=None,
        metadata={
            "name": "Package",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/batch/init/request/2021/10/01/0001",
            "required": True,
        },
    )
    package_file_hash: Optional[PackageFileHashType] = field(
        default=None,
        metadata={
            "name": "PackageFileHash",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/batch/init/request/2021/10/01/0001",
            "required": True,
        },
    )
    package_parts_list: Optional[
        "PackageSignatureInitRequestType.PackagePartsList"
    ] = field(
        default=None,
        metadata={
            "name": "PackagePartsList",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/batch/init/request/2021/10/01/0001",
            "required": True,
        },
    )

    @dataclass
    class PackagePartsList:
        package_part_signature: List[PackagePartSignatureInitRequestType] = (
            field(
                default_factory=list,
                metadata={
                    "name": "PackagePartSignature",
                    "type": "Element",
                    "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/batch/init/request/2021/10/01/0001",
                    "min_occurs": 1,
                    "max_occurs": 100,
                },
            )
        )


@dataclass
class InitRequest:
    class Meta:
        namespace = "http://ksef.mf.gov.pl/schema/gtw/svc/batch/init/request/2021/10/01/0001"

    identifier: Optional[SubjectIdentifierByType] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        },
    )
    document_type: Optional[DocumentTypeType] = field(
        default=None,
        metadata={
            "name": "DocumentType",
            "type": "Element",
            "required": True,
        },
    )
    encryption: Optional[EncryptionType] = field(
        default=None,
        metadata={
            "name": "Encryption",
            "type": "Element",
            "required": True,
        },
    )
    package_signature: Optional[PackageSignatureInitRequestType] = field(
        default=None,
        metadata={
            "name": "PackageSignature",
            "type": "Element",
            "required": True,
        },
    )
