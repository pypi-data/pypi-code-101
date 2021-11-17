import json
from typing import List

from cloudprice.azure_helpers import ODataFactory, ValidationFactory
from cloudprice.prices import AzurePrice


class AzureVM:
    def __init__(self, region: str, arm_sku_name: str):
        self.vm_price_list: List[AzurePrice] = []
        self.odata_factory = ODataFactory()
        self.defaultFilters = [
            self.odata_factory.equalsFilter("serviceName", "Virtual Machines")
        ]
        self.__getVmPrices(region, arm_sku_name)

    def __filterForOs(self, azure_price: List[AzurePrice], os: str) -> List[AzurePrice]:
        ValidationFactory.validateOsType(os)

        if os == "Linux":
            return filter(lambda x: "Windows" not in x.product_name, azure_price)
        else:
            return filter(lambda x: "Windows" in x.product_name, azure_price)

    def __filterForVmType(
        self, azure_price: List[AzurePrice], vm_type: str
    ) -> List[AzurePrice]:
        ValidationFactory.validateVMType(vm_type)

        if vm_type == "Spot":
            return filter(lambda x: "Spot" in x.meter_name, azure_price)
        elif vm_type == "LowPriority":
            return filter(lambda x: "Low Priority" in x.meter_name, azure_price)
        else:
            return filter(
                lambda x: (
                    "Spot" not in x.meter_name and "Low Priority" not in x.meter_name
                ),
                azure_price,
            )

    def __getVmPrices(self, region: str, arm_sku_name: str):
        ValidationFactory.validateRegion(region)

        filters = self.defaultFilters
        filters.extend(
            [
                self.odata_factory.equalsFilter("armSkuName", arm_sku_name),
                self.odata_factory.equalsFilter("location", region),
            ]
        )

        request_uri = self.odata_factory.buildURI(filters)

        response = self.odata_factory.submitQuery(request_uri)
        # TODO: Check to see if there is any need to paginate. Field to check is response["NextPageLink"]

        response_items = response["Items"]

        self.vm_price_list = []
        for item in response_items:
            x = json.dumps(item)
            price_dict = json.loads(x)
            price_object = AzurePrice(**price_dict)
            self.vm_price_list.append(price_object)

    def __handleReservations(
        self, price_list: List[AzurePrice], reservation_term: str
    ) -> AzurePrice:
        ValidationFactory.validateReservationTerm(reservation_term)

        if reservation_term == "1YR":
            reservation_price = list(
                filter(lambda x: x.reservation_term == "1 Year", price_list)
            )[0]
            reservation_price.unit_price = reservation_price.unit_price / 365 / 24
        elif reservation_term == "3YR":
            reservation_price = list(
                filter(lambda x: x.reservation_term == "3 Years", price_list)
            )[0]
            reservation_price.unit_price = reservation_price.unit_price / 3 / 365 / 24
        return reservation_price

    def __handleOnDemand(self, price_list: List[AzurePrice], os: str, vm_type: str):
        price_filtered_for_os = self.__filterForOs(price_list, os)

        # Filter based on VM Type
        price_filtered_for_vm_type = self.__filterForVmType(
            price_filtered_for_os, vm_type
        )

        on_demand_price_list = list(price_filtered_for_vm_type)[0]

        return on_demand_price_list

    def getLatestPrice(
        self,
        os="Linux",
        vm_type="Standard",
        vm_pricing_type="Consumption",
        reservation_term="1YR",
    ):
        # Check Pricing Type to see if valid
        ValidationFactory.validateVMPricingType(vm_pricing_type)

        # Filter based on Pricing Type
        price_filtered_pricing_type: List[AzurePrice] = filter(
            lambda x: x.type == vm_pricing_type, self.vm_price_list
        )

        # Handle VM Pricing Types
        try:
            if vm_pricing_type == "Reservation":
                price = self.__handleReservations(
                    price_filtered_pricing_type, reservation_term
                )

            else:
                price = self.__handleOnDemand(price_filtered_pricing_type, os, vm_type)
            return price

        except:
            raise ValueError(
                f"""
            No prices found for the inputs provided:
            OS: {os}
            VM Type: {vm_type}
            VM Pricing Tier: {vm_pricing_type}     
            """
            )
