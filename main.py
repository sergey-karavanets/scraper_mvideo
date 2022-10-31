import requests
import json


def get_data():
    cookies = {
        'HINTS_FIO_COOKIE_NAME': '2',
        'MVID_AB_SERVICES_DESCRIPTION': 'var4',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CART_MULTI_DELETE': 'false',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityCZ_9912',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GUEST_ID': '21505223523',
        'MVID_HANDOVER_SUMMARY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '2200000100000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_MOBILE_FILTERS': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_ID': '37',
        'MVID_REGION_SHOP': 'S933',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
        'MVID_TIMEZONE_OFFSET': '7',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'searchType2': '2',
        'MVID_AB_TOP_SERVICES': '2',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        '__ttl__widget__ui': '1665138144671-265447afc966',
        'wurfl_device_id': 'generic_web_browser',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'deviceType': 'desktop',
        'MVID_COMPARE_LIST': '50038582/50041640',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VSVzc5IUhiOwtsCRRlOzMxbDoNR1EaWVQ7HytVEUVlCXk/RyVOIWk9EkIrPlE/TBpwWDs7GjhmJmZKWyhEWFB/FhoXfXAkUg8MYD9KbnQbN1ddHBEkWA4hPwtpW1Y0ZxUbQEgYL0tueS9AZiBnSWAlQ1hTdRdgSkMrNhZGRhxyM3c/awgiGVETKl94R1drZVVCODFnDE9PTRIWBZO+TQ==',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VSVzc5IUhiOwtsCRRlOzMxbDoNR1EaWVQ7HytVEUVlCXk/RyVOIWk9EkIrPlE/TBpwWDs7GjhmJmZKWyhEWFB/FhoXfXAkUg8MYD9KbnQbN1ddHBEkWA4hPwtpW1Y0ZxUbQEgYL0tueS9AZiBnSWAlQ1hTdRdgSkMrNhZGRhxyM3c/awgiGVETKl94R1drZVVCODFnDE9PTRIWBZO+TQ==',
        'cfidsgib-w-mvideo': 'oWsl8/NbdvIp6wwYadhmkpAkMD1FgLuCUs32fvB1SoiyW2vGMddP9rx5ZuxC6mTcQv7tSZqCpk5dlVNBi1b3/qU9hBOXY/Z++0o7U80QQpKpc9r9AIEHXBiywUgHRpj4/pNc6mlgIjcJ6BREDJ1OVepwfO0dw+2ZhHlx',
        'cfidsgib-w-mvideo': 'oWsl8/NbdvIp6wwYadhmkpAkMD1FgLuCUs32fvB1SoiyW2vGMddP9rx5ZuxC6mTcQv7tSZqCpk5dlVNBi1b3/qU9hBOXY/Z++0o7U80QQpKpc9r9AIEHXBiywUgHRpj4/pNc6mlgIjcJ6BREDJ1OVepwfO0dw+2ZhHlx',
        'gsscgib-w-mvideo': 'Oz9sNPDm1IJCbt1X4UBbDxYkcyYifhV/sUmKkECKGblXmJkdbqTorJynZyBAZROBpwxM+lfo2P5noKsqpbNg0xt/1hiTGMYsHLtyhmD6d5UsIdYI210DSA1BqKLKmCGJf1DAef1WI+YNtAc0jQs4hp++g78rxZ4BbmTKVTQWgRroPelwvPceQKaVDZCvtmd6twUTyT7O9wYE7w/jj3NrhhHsFl+i3ZeCn+55mMyutclpe0s5iKe5WNJM8eG2QA==',
        'gsscgib-w-mvideo': 'Oz9sNPDm1IJCbt1X4UBbDxYkcyYifhV/sUmKkECKGblXmJkdbqTorJynZyBAZROBpwxM+lfo2P5noKsqpbNg0xt/1hiTGMYsHLtyhmD6d5UsIdYI210DSA1BqKLKmCGJf1DAef1WI+YNtAc0jQs4hp++g78rxZ4BbmTKVTQWgRroPelwvPceQKaVDZCvtmd6twUTyT7O9wYE7w/jj3NrhhHsFl+i3ZeCn+55mMyutclpe0s5iKe5WNJM8eG2QA==',
        'fgsscgib-w-mvideo': '9aQdc53ca2363a57f8972fea4ea1c18bce20d56e',
        'fgsscgib-w-mvideo': '9aQdc53ca2363a57f8972fea4ea1c18bce20d56e',
        'cfidsgib-w-mvideo': 'Zw4MREjUUevZgBAQmvIpKsMJ/zR55ZO9GPKhpDj7/t4RXyqqD5+Hgg/JmVNwAOQEAJLK1n94hKEDtd2FW/HU2EPhdEeTCYzpDOHWSxvVnPkvD6H4eMoCt/J17Wpzk8CuMl4kT/A3pMcn3c2FAQT3kpHQ14mzl3RsY16oQQ==',
        'CACHE_INDICATOR': 'false',
        'COMPARISON_INDICATOR': 'false',
        'MVID_AB_PDP_CHAR': '2',
        'MVID_GLC': 'true',
        'MVID_GLP': 'true',
        'mindboxDeviceUUID': 'ff4ab22c-e468-4f21-8f07-2e4dfb17ece6',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22ff4ab22c-e468-4f21-8f07-2e4dfb17ece6%22%7D',
        '__lhash_': 'e1366ab48c9ea3d0535607b4e0a635e4',
        'flacktory': 'no',
        'JSESSIONID': 'pjXXjfTbGBVGJ1cD6rXvGStnMhn4RjJqv7p2VKqsXhnTpBydq0k9!-1059248804',
        'bIPs': '-1991023829',
        'MVID_ENVCLOUD': 'prod2',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-RU;q=0.8,en;q=0.7,en-US;q=0.6',
        'baggage': 'sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=91e430f8b4b34477b641cc3d4e748975,sentry-sample_rate=0%2C5',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'HINTS_FIO_COOKIE_NAME=2; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CART_AVAILABILITY=true; MVID_CART_MULTI_DELETE=false; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_9912; MVID_CREDIT_AVAILABILITY=true; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GUEST_ID=21505223523; MVID_HANDOVER_SUMMARY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=2200000100000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=37; MVID_REGION_SHOP=S933; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_TIMEZONE_OFFSET=7; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; searchType2=2; MVID_AB_TOP_SERVICES=2; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_MINDBOX_DYNAMICALLY=true; __ttl__widget__ui=1665138144671-265447afc966; wurfl_device_id=generic_web_browser; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; deviceType=desktop; MVID_COMPARE_LIST=50038582/50041640; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VSVzc5IUhiOwtsCRRlOzMxbDoNR1EaWVQ7HytVEUVlCXk/RyVOIWk9EkIrPlE/TBpwWDs7GjhmJmZKWyhEWFB/FhoXfXAkUg8MYD9KbnQbN1ddHBEkWA4hPwtpW1Y0ZxUbQEgYL0tueS9AZiBnSWAlQ1hTdRdgSkMrNhZGRhxyM3c/awgiGVETKl94R1drZVVCODFnDE9PTRIWBZO+TQ==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VSVzc5IUhiOwtsCRRlOzMxbDoNR1EaWVQ7HytVEUVlCXk/RyVOIWk9EkIrPlE/TBpwWDs7GjhmJmZKWyhEWFB/FhoXfXAkUg8MYD9KbnQbN1ddHBEkWA4hPwtpW1Y0ZxUbQEgYL0tueS9AZiBnSWAlQ1hTdRdgSkMrNhZGRhxyM3c/awgiGVETKl94R1drZVVCODFnDE9PTRIWBZO+TQ==; cfidsgib-w-mvideo=oWsl8/NbdvIp6wwYadhmkpAkMD1FgLuCUs32fvB1SoiyW2vGMddP9rx5ZuxC6mTcQv7tSZqCpk5dlVNBi1b3/qU9hBOXY/Z++0o7U80QQpKpc9r9AIEHXBiywUgHRpj4/pNc6mlgIjcJ6BREDJ1OVepwfO0dw+2ZhHlx; cfidsgib-w-mvideo=oWsl8/NbdvIp6wwYadhmkpAkMD1FgLuCUs32fvB1SoiyW2vGMddP9rx5ZuxC6mTcQv7tSZqCpk5dlVNBi1b3/qU9hBOXY/Z++0o7U80QQpKpc9r9AIEHXBiywUgHRpj4/pNc6mlgIjcJ6BREDJ1OVepwfO0dw+2ZhHlx; gsscgib-w-mvideo=Oz9sNPDm1IJCbt1X4UBbDxYkcyYifhV/sUmKkECKGblXmJkdbqTorJynZyBAZROBpwxM+lfo2P5noKsqpbNg0xt/1hiTGMYsHLtyhmD6d5UsIdYI210DSA1BqKLKmCGJf1DAef1WI+YNtAc0jQs4hp++g78rxZ4BbmTKVTQWgRroPelwvPceQKaVDZCvtmd6twUTyT7O9wYE7w/jj3NrhhHsFl+i3ZeCn+55mMyutclpe0s5iKe5WNJM8eG2QA==; gsscgib-w-mvideo=Oz9sNPDm1IJCbt1X4UBbDxYkcyYifhV/sUmKkECKGblXmJkdbqTorJynZyBAZROBpwxM+lfo2P5noKsqpbNg0xt/1hiTGMYsHLtyhmD6d5UsIdYI210DSA1BqKLKmCGJf1DAef1WI+YNtAc0jQs4hp++g78rxZ4BbmTKVTQWgRroPelwvPceQKaVDZCvtmd6twUTyT7O9wYE7w/jj3NrhhHsFl+i3ZeCn+55mMyutclpe0s5iKe5WNJM8eG2QA==; fgsscgib-w-mvideo=9aQdc53ca2363a57f8972fea4ea1c18bce20d56e; fgsscgib-w-mvideo=9aQdc53ca2363a57f8972fea4ea1c18bce20d56e; cfidsgib-w-mvideo=Zw4MREjUUevZgBAQmvIpKsMJ/zR55ZO9GPKhpDj7/t4RXyqqD5+Hgg/JmVNwAOQEAJLK1n94hKEDtd2FW/HU2EPhdEeTCYzpDOHWSxvVnPkvD6H4eMoCt/J17Wpzk8CuMl4kT/A3pMcn3c2FAQT3kpHQ14mzl3RsY16oQQ==; CACHE_INDICATOR=false; COMPARISON_INDICATOR=false; MVID_AB_PDP_CHAR=2; MVID_GLC=true; MVID_GLP=true; mindboxDeviceUUID=ff4ab22c-e468-4f21-8f07-2e4dfb17ece6; directCrm-session=%7B%22deviceGuid%22%3A%22ff4ab22c-e468-4f21-8f07-2e4dfb17ece6%22%7D; __lhash_=e1366ab48c9ea3d0535607b4e0a635e4; flacktory=no; JSESSIONID=pjXXjfTbGBVGJ1cD6rXvGStnMhn4RjJqv7p2VKqsXhnTpBydq0k9!-1059248804; bIPs=-1991023829; MVID_ENVCLOUD=prod2',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195/f/skidka=da/tolko-v-nalichii=da',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '91e430f8b4b34477b641cc3d4e748975-8ddd919dd27b2d0d-1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'x-set-application-id': 'a25a81d8-9472-4cad-a435-ade8ad8b18d6',
    }

    params = {
        'categoryId': '195',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()

    products_ids = response.get('body').get('products')

    with open('1_products_ids.json', 'w', encoding='utf-8') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    json_data = {
            'productIds': products_ids,
            'mediaTypes': [
                'images',
            ],
            'category': True,
            'status': True,
            'brand': True,
            'propertyTypes': [
                'KEY',
            ],
            'propertiesConfig': {
                'propertiesPortionSize': 5,
            },
            'multioffer': False,
        }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                                 json=json_data).json()

    with open('2_items.json', 'w', encoding='utf-8') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    products_ids_str = ','.join(products_ids)

    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()

    with open('3_prices.json', 'w', encoding='utf-8') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_prices = {}

    material_prices = response.get('body').get('materialPrices')

    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        items_prices[item_id] = {
            'item_basePrice': item_base_price,
            'item_salePrice': item_sale_price,
            'item_bonus': item_bonus
        }

    with open('4_items_prices.json', 'w', encoding='utf-8') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)

def get_result():
    pass

def main():
    get_data()


if __name__ == '__main__':
    main()