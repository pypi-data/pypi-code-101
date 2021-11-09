from .test_constants import (TEST_COLLECTION_CONTRACT_ADDRESS,
                             TEST_MARKET_CONTRACT_ADDRESS,
                             TEST_NFT_CONTRACT_ADDRESS)
import unittest

from nftlabs import NftlabsSdk, SdkOptions
from nftlabs.abi.market import MarketListing


class TestMarket(unittest.TestCase):
    def test_init_marketplace_module(self):
        """
        Test that tries to instantiate the Marketplace module
        """
        sdk = NftlabsSdk(SdkOptions(), "https://rpc-mumbai.maticvigil.com")
        market_module = sdk.get_market_module(TEST_MARKET_CONTRACT_ADDRESS)

        self.assertFalse(market_module.is_erc721(
            TEST_COLLECTION_CONTRACT_ADDRESS), "A collection is not a 721 contract")
        self.assertTrue(market_module.is_erc721(
            TEST_NFT_CONTRACT_ADDRESS), "A nft contract is a 721 contract")

        self.assertTrue(market_module.is_erc1155(
            TEST_COLLECTION_CONTRACT_ADDRESS), "A collection is a 1155 contract")
        self.assertFalse(market_module.is_erc1155(
            TEST_NFT_CONTRACT_ADDRESS), "A nft contract is not a 1155 contract")

    # def test___transform_result_to_listing(self):
    #     sdk = NftlabsSdk(SdkOptions(), "https://rpc-mumbai.maticvigil.com")
    #     market_module = sdk.get_market_module(TEST_MARKET_CONTRACT_ADDRESS)

    #     test_listing = MarketListing(
    #         listingId=6,
    #         seller="0xE79ee09bD47F4F5381dbbACaCff2040f2FbC5803",
    #         assetContract="0x5CF412451f4Cef34293604048238bd18D2BD1e71",
    #         tokenId=1,
    #         quantity=1,
    #         currency="0x0000000000000000000000000000000000000000",
    #         pricePerToken=0,
    #         saleStart=1636463066,
    #         saleEnd=1636463066,
    #         tokensPerBuyer=1,
    #         tokenType=0
    #     )
    #     print("OKOK", test_listing.currency)
    #     result = market_module._MarketModule__transform_result_to_listing(
    #         test_listing)
    #     print("RESULT = result", result)
