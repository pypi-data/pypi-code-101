import functools
from typing import List, Any

from zeep import Client
from urllib.parse import urljoin

from zeep.xsd import ComplexType

from .helpers import modify_url_for_urljoin
from .model import Identity


def create_epix_client(base_url: str) -> Client:
    """
    Creates a Zeep client for the E-PIX SOAP interface hosted at the given URL.

    :param base_url: URL where the E-PIX service is hosted
    :return: Zeep client
    """
    wsdl_url = urljoin(modify_url_for_urljoin(base_url), "epixService?wsdl")
    return Client(wsdl_url)


def get_identity_type(client: Client) -> ComplexType:
    """
    Returns the identity type as defined by the SOAP interface.

    :param client: Zeep client with E-PIX SOAP methods
    :return: SOAP identity type
    """
    return client.get_type("ns0:identityInDTO")


def get_mpi_request_type(client: Client) -> ComplexType:
    """
    Returns the MPI request type as defined by the SOAP interface.

    :param client: Zeep client with E-PIX SOAP methods
    :return: SOAP MPI request type
    """
    return client.get_type("ns0:mpiRequestDTO")


def _get_mpi_from_mpi_batch_response_entry(entry: Any) -> str:
    return entry.value.person.mpiId.value


def request_mpi_batch(client: Client, domain: str, source: str, identities: List[Identity]):
    """
    Submits many identities to the MPI for creation. Returns the identifiers assigned to these identities.

    :param client: Zeep client with E-PIX SOAP methods
    :param domain: Data domain
    :param source: Data source
    :param identities: Identities to insert
    :return: List of identifiers
    """
    create_soap_mpi_batch_request = get_mpi_request_type(client)
    create_soap_identity = get_identity_type(client)

    entries = [
        create_soap_identity(
            firstName=i.first_name,
            lastName=i.last_name,
            birthDate=i.birth_date,
            gender=i.gender,
            birthPlace=i.birth_place,
            civilStatus=i.civil_status,
            degree=i.degree,
            externalDate=i.external_date,
            middleName=i.middle_name,
            motherTongue=i.mother_tongue,
            mothersMaidenName=i.mothers_maiden_name,
            nationality=i.nationality,
            prefix=i.prefix,
            race=i.race,
            religion=i.religion,
            suffix=i.suffix
        ) for i in identities
    ]

    request = create_soap_mpi_batch_request(
        domainName=domain,
        sourceName=source,
        requestEntries=entries
    )

    response = client.service.requestMPIBatch(request)

    if response is None:
        return []

    return [
        _get_mpi_from_mpi_batch_response_entry(e) for e in response.entry
    ]


def _get_identity_id_from_person_for_domain_response_entry(entry: Any) -> int:
    """

    :param entry:
    :return:
    """
    return entry.referenceIdentity.identityId


def get_identity_ids_in_domain(client: Client, domain: str) -> List[int]:
    """
    Fetches all identity IDs present in the given domain.

    :param client: Zeep client with E-PIX SOAP methods
    :param domain: Data domain
    :return: List of identity IDs
    """
    response = client.service.getPersonsForDomain(domain)
    return [
        _get_identity_id_from_person_for_domain_response_entry(e) for e in response
    ]


def delete_identity(client: Client, identity_id: int) -> None:
    """
    Deletes the identity with the given ID.

    :param client: Zeep client with E-PIX SOAP methods
    :param identity_id: ID of the identity to delete
    """
    client.service.deleteIdentity(identity_id)


def deactivate_identity(client: Client, identity_id: int) -> None:
    """
    Deactivates the identity with the given ID.

    :param client: Zeep client with E-PIX SOAP methods
    :param identity_id: ID of the identity to deactivate
    """
    client.service.deactivateIdentity(identity_id)


def resolve_person_for_mpi(client: Client, domain: str, mpi: str) -> Identity:
    """
    Looks up an identifier in the MPI and returns the corresponding personal entry, if present.

    :param client: Zeep client with E-PIX SOAP methods
    :param domain: Data domain
    :param mpi: MPI record identifier
    :return: Personal data associated with the given identifier
    """
    person_data = client.service.getPersonByMPI(domain, mpi)
    person_data_id = person_data["referenceIdentity"]

    first_name = str(person_data_id["firstName"])
    last_name = str(person_data_id["lastName"])
    birth_date = person_data_id["birthDate"]
    gender = str(person_data_id["gender"])
    civil_status = person_data_id["civilStatus"]
    degree = person_data_id["degree"]
    external_date = person_data_id["externalDate"]
    middle_name = person_data_id["middleName"]
    mother_tongue = person_data_id["motherTongue"]
    mothers_maiden_name = person_data_id["mothersMaidenName"]
    nationality = person_data_id["nationality"]
    prefix = person_data_id["prefix"]
    race = person_data_id["race"]
    religion = person_data_id["religion"]
    suffix = person_data_id["suffix"]

    return Identity(first_name, last_name, gender, birth_date, civil_status, degree, external_date, middle_name,
                    mother_tongue, mothers_maiden_name, nationality, prefix, race, religion, suffix)


class EPIXClient:

    def __init__(self, base_url: str):
        """
        Creates a convenience wrapper around selected E-PIX SOAP functions.

        :param base_url: URL where the E-PIX service is hosted
        """
        client = create_epix_client(base_url)
        self.resolve_person_for_mpi = functools.partial(resolve_person_for_mpi, client)
        self.request_mpi_batch = functools.partial(request_mpi_batch, client)
        self.get_mpis_in_domain = functools.partial(get_identity_ids_in_domain, client)
        self.delete_identity = functools.partial(delete_identity, client)
        self.deactivate_identity = functools.partial(deactivate_identity, client)
