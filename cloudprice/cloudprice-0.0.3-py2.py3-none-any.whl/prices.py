from dataclasses import dataclass


@dataclass(init=False)
class AzurePrice:
    def __init__(
        self,
        currencyCode,
        tierMinimumUnits,
        retailPrice,
        unitPrice,
        armRegionName,
        location,
        effectiveStartDate,
        meterId,
        meterName,
        productId,
        skuId,
        productName,
        skuName,
        serviceName,
        serviceId,
        serviceFamily,
        unitOfMeasure,
        type,
        isPrimaryMeterRegion,
        armSkuName,
        reservationTerm=None,
        effectiveEndDate=None,
        **kwargs
    ):
        self.currency_code = currencyCode
        self.tier_min_units = tierMinimumUnits
        self.retail_price = retailPrice
        self.unit_price = unitPrice
        self.arm_region_name = armRegionName
        self.location = location
        self.effective_start_date = effectiveStartDate
        self.effective_end_date = effectiveEndDate
        self.meter_id = meterId
        self.meter_name = meterName
        self.product_id = productId
        self.sku_id = skuId
        self.product_name = productName
        self.reservation_term = reservationTerm
        self.sku_name = skuName
        self.service_name = serviceName
        self.service_id = serviceId
        self.service_family = serviceFamily
        self.unit_of_measure = unitOfMeasure
        self.type = type
        self.is_primary_meter_region = isPrimaryMeterRegion
        self.arn_sku_name = armSkuName

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
