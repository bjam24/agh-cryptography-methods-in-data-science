from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from generated.types.pkg_2021.pkg_10.pkg_01.pkg_0001.gtw_types import (
    AccountNumberType,
    AuthorisationTypeType,
    DocumentTypeType,
    EncryptionType,
    SubjectIdentifierByType,
    SubjectIdentifierToType,
)

__NAMESPACE__ = (
    "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001"
)


@dataclass
class InvoicePaymentConfirmationTokenType:
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Timestamp",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
            "required": True,
            "min_inclusive": XmlDateTime(2022, 1, 1, 0, 0, 0, 0, 60),
            "white_space": "collapse",
        },
    )
    unique_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "UniqueID",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        },
    )
    booking_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BookingDate",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
            "required": True,
            "min_inclusive": XmlDate(2022, 1, 1),
            "white_space": "collapse",
        },
    )
    currency_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurrencyCode",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
            "required": True,
            "pattern": r"[A-Z]{2,3}",
        },
    )
    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
            "required": True,
            "total_digits": 12,
            "fraction_digits": 2,
        },
    )
    payment_subject: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentSubject",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class AuthorisationContextType:
    challenge: Optional[str] = field(
        default=None,
        metadata={
            "name": "Challenge",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
            "required": True,
            "pattern": r"(20[2-9][0-9]|2[1-9][0-9]{2}|[3-9][0-9]{3})(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])-([0-9A-Z]{2})-([0-9A-F]{10})-([0-9A-F]{10})-([0-9A-F]{2})",
        },
    )
    identifier: Optional[SubjectIdentifierByType] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
            "required": True,
        },
    )
    document_type: Optional[DocumentTypeType] = field(
        default=None,
        metadata={
            "name": "DocumentType",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
            "required": True,
        },
    )
    encryption: Optional[EncryptionType] = field(
        default=None,
        metadata={
            "name": "Encryption",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
        },
    )


@dataclass
class InvoicePaymentConfirmationTokenBankType(
    InvoicePaymentConfirmationTokenType
):
    source_account_number: Optional[AccountNumberType] = field(
        default=None,
        metadata={
            "name": "SourceAccountNumber",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
            "required": True,
        },
    )
    destination_account_number: Optional[AccountNumberType] = field(
        default=None,
        metadata={
            "name": "DestinationAccountNumber",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
            "required": True,
        },
    )


@dataclass
class InvoicePaymentConfirmationTokenCardType(
    InvoicePaymentConfirmationTokenType
):
    card4_digits: Optional[str] = field(
        default=None,
        metadata={
            "name": "Card4Digits",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
            "required": True,
            "min_length": 4,
            "max_length": 4,
        },
    )
    destination_identifier: Optional[SubjectIdentifierByType] = field(
        default=None,
        metadata={
            "name": "DestinationIdentifier",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
        },
    )
    destination_account_number: Optional[AccountNumberType] = field(
        default=None,
        metadata={
            "name": "DestinationAccountNumber",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
            "required": True,
        },
    )


@dataclass
class InvoicePaymentConfirmationTokenDirectType(
    InvoicePaymentConfirmationTokenType
):
    payment_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentType",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
            "required": True,
            "min_length": 1,
            "max_length": 64,
        },
    )
    source_identifier: Optional[SubjectIdentifierToType] = field(
        default=None,
        metadata={
            "name": "SourceIdentifier",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
            "required": True,
        },
    )
    destination_identifier: Optional[SubjectIdentifierByType] = field(
        default=None,
        metadata={
            "name": "DestinationIdentifier",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
            "required": True,
        },
    )


@dataclass
class InvoicePaymentConfirmationTokenFaktorType(
    InvoicePaymentConfirmationTokenType
):
    source_identifier: Optional[SubjectIdentifierToType] = field(
        default=None,
        metadata={
            "name": "SourceIdentifier",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
            "required": True,
        },
    )
    destination_identifier: Optional[SubjectIdentifierByType] = field(
        default=None,
        metadata={
            "name": "DestinationIdentifier",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
            "required": True,
        },
    )
    destination_account_number: Optional[AccountNumberType] = field(
        default=None,
        metadata={
            "name": "DestinationAccountNumber",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
        },
    )


@dataclass
class InvoicePaymentConfirmationTokenOnlineType(
    InvoicePaymentConfirmationTokenType
):
    service_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceType",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
            "required": True,
            "min_length": 1,
            "max_length": 64,
        },
    )
    destination_identifier: Optional[SubjectIdentifierByType] = field(
        default=None,
        metadata={
            "name": "DestinationIdentifier",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
        },
    )
    destination_account_number: Optional[AccountNumberType] = field(
        default=None,
        metadata={
            "name": "DestinationAccountNumber",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
            "required": True,
        },
    )


@dataclass
class AuthorisationContextSignedType(AuthorisationContextType):
    type_value: Optional[AuthorisationTypeType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
            "required": True,
        },
    )


@dataclass
class AuthorisationContextTokenType(AuthorisationContextType):
    """
    :ivar token: Authorisation token bytes encrypted with service
        certificate public key (transformation RSA/ECB/PKCS#1) and then
        encoded with Base64
    """

    token: Optional[str] = field(
        default=None,
        metadata={
            "name": "Token",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
            "required": True,
            "min_length": 344,
            "max_length": 344,
        },
    )
