import join_lounge
import get_client_id
import get_token
import json

# uid列表，用来去获取client_id
uid_list = ['u1592560688671743535']
token_list = [
    'MTU5MjU2MDY4OHxEM3ZNd0poRkpvWkN6QmQwdU03aThDZWZaOW1qb0RMOHJUZGREci1xakIxMnlSX0gtRWt0Q1ZSREhLREU2RGUtMHpvNnVGNmhLeVJGdkRfa2x0aFM1YktYTGZ1RUNDbWZ8075exn7Hw5Gcrvm1wSkHHkAy-INMx1yZYd1ExzKvwHA=']

# uid_list = [ 'u1592560688671743535', 'u1592560689318259154', 'u1592560689997511820', 'u1592560690629720849',
#              'u1592560691246881650', 'u1592560692022567635', 'u1592560692652402980', 'u1592560693259152702',
#              'u1592560693818984518', 'u1592560694448749296', 'u1592560695156670182', 'u1592560695760195005',
#              'u1592560696414063307', 'u1592560697062116772', 'u1592560697948462267', 'u1592560698685657468',
#              'u1592560699404356443', 'u1592560700190326902', 'u1592560700851255942', 'u1592560701850536892',
#              'u1592560702744942402', 'u1592560703438585615', 'u1592560704185207587', 'u1592560704926935053',
#              'u1592560705683496871', 'u1592560706477608006', 'u1592560707094624564', 'u1592560707757411855',
#              'u1592560708458813665', 'u1592560709062099482', 'u1592560709693807613', 'u1592560710286855410',
#              'u1592560710910079473', 'u1592560711538942891', 'u1592560712160641180', 'u1592560712741470246',
#              'u1592560714317413313', 'u1592560714872392134', 'u1592560715454481716', 'u1592560716024817151',
#              'u1592560716629893310', 'u1592560717223822915', 'u1592560717834896825', 'u1592560718475509551',
#              'u1592560719075992008', 'u1592560719686924388', 'u1592560720231338830', 'u1592560720901608938',
#              'u1592560721649425115', 'u1592560722364911547','u1592574141776159067', 'u1592574142402886141']

# uid对应各token列表
# token_list = [
#     'MTU5MjU2MDY4OHxEM3ZNd0poRkpvWkN6QmQwdU03aThDZWZaOW1qb0RMOHJUZGREci1xakIxMnlSX0gtRWt0Q1ZSREhLREU2RGUtMHpvNnVGNmhLeVJGdkRfa2x0aFM1YktYTGZ1RUNDbWZ8075exn7Hw5Gcrvm1wSkHHkAy-INMx1yZYd1ExzKvwHA=',
#     'MTU5MjU2MDY4OXxDbzE5S1VHMm83elpwUTV1UzVibFFpM25PRjJfMFJHS2dkczJTNlJPNDlnYS1YRVRFNnZoQ2liMlpyalM5SEZIemVnNzI3RjhMaVU2RXhGTXpZQm05S1p6RmRtQ2pEUlh8p5er7oHPyxz7VWXKyBgLYwOp9szklM5P2IVZKmRxDz0=',
#     'MTU5MjU2MDY5MHwzYVEtNmRXbk5jOUg0YUljaXROdjcxNFRTVmNmWUNXQXJxeXM2Q3dPSmE2SFpMZndXaV9TQTU4amZPb3BSS29xLWd5QXlmQnQyS2RaR0ZXVC1vOW44VVpCNHNnWU5pYkR8zmg1L-QAG6tcNfHSHHKTWio890_V_w3WEqB9xKOH82s=',
#     'MTU5MjU2MDY5MHx5QXkxZUdnZ21yR0VXb1NyX1hGNFZjalhkdURTNVduSzFwdl9Zc05CUXNwSW45Z0dJcDZEQ1oyUnpGRjJuMW8xOEFKNTNsMlVfVjFxVXFtTXlHdXJSUThueU5jYUZ0N2R8A-fy8oTH0OHAvqIN6gyDL3aWVDOZZwC_0KWK8ZV1DdA=',
#     'MTU5MjU2MDY5MXxqV3liS2dKakM0U1RGTkJYcnBwa3R4U0lZZXN5bm02akZHT25kaDJKMzlrOGdSeklvVU5NM3FxLWhuU1dhRGZhbTV5ZG90SUdOd196U2I1YkFCaUVvTW4tN2JwNTROT3V8MWj-WCd9ipsRPfZzqA-8xtJe0Sn-z6rf4RTx_1dqRuI=',
#     'MTU5MjU2MDY5Mnx4VlQ3dUk4aFAzU1N6eUNhR2pyU1M0ZXZ0UkNGTDJEWFNnWlhSbU5aaXFTU0hTd1RKNng5WFR3d1hnUWtIRXFXZ0I4MkVKUHNTZnM1dXhxeWJXM3FtY1J3MjNGelNKNDl8Tcbp6k05nSWuGZEPEfPhVBE07JMqIXWklU_3ud5r-uE=',
#     'MTU5MjU2MDY5Mnx4ZjNaU0pNUG1QWWJMWDVCOUVZNW5NZGlDOVhacXlydDFIZERDRlZUWGk1VFk2Z0F6Q1ZDNThpWGU4bnZ3WEtmT2dKUmF3MThkaVkzRDM5Rzh3Q1g4VjlJOUptUlhGbk98rke_lJeUg-NqPYT_C3rEl6WcR7ggCrxLsoo66A2MVA4=',
#     'MTU5MjU2MDY5M3wyRndiOUNzSmZyUXdwUFB1QzRCX3FzZk16ZzhmckNpeXVnWmNCQjYyRFV2UGJOZzBmbGVINjAxbnlJeHg0TVhTd1g1RnVVSDVpWVBIYXVlaTE4ZDBVa01kdDhPUGJBNW18xmWgXBsmwZVFvxWFKEotggqrOdbN0Q_ENO50zUulbBE=',
#     'MTU5MjU2MDY5M3xFV3pFckRhWmllRERDREU3aklQdC1OMFctai1ocjZUS3o4N0FPZUl2R0JVdVdRVWdVX1paSWlqcnpESmFXek96SXVOX1dCN25pb19xUDNrbUdZSnBHMU9vRzY0US1BZlp8KQAMK1jGOkB2TApo4gwKqV8OyIs8OzPOhmiLipgXPS4=',
#     'MTU5MjU2MDY5NHw1MW9qYlNOcjRqLUZMLWxkRHpfa3dhNV9KekgtY1ZsMHV4cjBNUkJJM2R0ZTYtZ0dVSk9naTNpRXBiOVg2RGswVXBmbnpfSjhOb0E2UkkyOTIwaXFtdHBNNlhfcnZIMGd8sdvM3EiqpSOd3X1NbHKVQInaVCEYQqHd9n7zPM0F_6U=',
#     'MTU5MjU2MDY5NXxJdnIxZHlHT2Zuajd6QzBWdy1rcjdBU3VKRGxGTl9OWmNOLTRIQ0RqNWx0SFItdk1VNWFCX0UzMllTbXRoa2FQLW9lWEN6aTIzT0F6aHNPdEl0clM5Q3VpdEExS3o4T2V8G_Tw7K9LOBNXJJCU_2__PGEHvy6o6Y-VIBicGkM94Wo=',
#     'MTU5MjU2MDY5NXwzWmhxX1BDZURHVFRYc1h4VlpiMU1QczBzSFBkalpQWEh4LW1naXBvdTh4RTJzVjZzVDJUc0VBQlZKaW9kR1hzcGQwaTIwUGpuY1dZNF8yUGV5UGRkUU14YXZJZTFIa0Z8GNJ99lPr9JUqA3DhOSRz4OS4sWELycpY6f_0SbsPKjQ=',
#     'MTU5MjU2MDY5Nnx5YnpjUFB5QjRYdXFrMEJNSTA1emowUWh0M0lqWUJrOG1ud250cmlQVTF5X05vUTBKaTlqY0lmaGdmM01BUWVCTXJEbUNKQ2RNMTZPaWJsbnpQVU5wOVVUNkt1N0swalR8am1HJ6TjXLFNXEzWGZuwvysKaPEY67M1zCRifmnFwwk=',
#     'MTU5MjU2MDY5N3xQNjFqTkZnWjVYTE11N1RSWUN6ZXJMb2xCYW9mOFZUZG5vTFdTclh4MkJMc3NVTl9lQUR2Q053UU1zRUpzeDFLYUk1WlA5SXFqYVV1OUxMYlNpdW96RnB0alNsWlp6QTh8zcaKa_unaaa60ZRB_f_I35ja2h43conYUu2F71Tu2QE=',
#     'MTU5MjU2MDY5OHxDQ3Z4TWZsWXBkQzhhdFQ0Z2RTaWxUZWJWS1BOa08wcHNsajlqQkhIMndKM3AwSTJZN3h3dDFmT3BqVENTaVJSR3V6TzZqNmN5eWFsRFR3LWNZQXp6OVZRX2NWV040NGd8Xz79E1ar7vghFy-QlhPdWeXBNj9YPkSP7xsy_p4fvew=',
#     'MTU5MjU2MDY5OHxQRzI3cFZXc0toSUR5bXZhRDhPVS10aEhZNnpOMEhQUG9NR01BUE9NUmpGVTcycFZqZ2h2Z1A1NGFnREhIQ1RTYm42d0ptMGFQdUVha0NZYU51U1lXVlhDUVd0QmIyRlF8c9uVQTPMQ2GS5LtSAPt4SeB3tYEylGy1zbW5aek_r-w=',
#     'MTU5MjU2MDY5OXx1STNvQlcyOWNlOXg3SXZ6T205djNYRXNzNzhVM0dWLXFqbGZEWHp2WkJkWEYyQjJ1NzlUdE5Ha3FDU3lRS25keUdaU2dubEs0QkJINjZPc1pTYkRzaVhER2tKRXV5bHB8ZEUGt5aFUwPIpRzywlf10U-2P05mnIP-SMaroVBZqTQ=',
#     'MTU5MjU2MDcwMHwyQnFnRnQyUzlYYnV3Y1FzOE5IOWp3eWhVSHA2ajhKWE1PUjh5MEhkV281YldTRzFGanJaX3hWQUNDSXdyMXhfbDFPbzd3U0ktUENucV92X2s5eVRjbEpUTHc2VU5vUTJ8oRDPwrCMlqstROC2CnhCOC0haE9tSv2m-G25K6GxxUg=',
#     'MTU5MjU2MDcwMXxCY2FIRzY4R2JHQ3lsbXNpY2x6d1hUMW5ocTg4OTJkdlJ1UFFKWnVnclJFdUx2R1dmT2ExSkZIRURIVjN1elBDMFdrS3Z0NVZ5ZzJiTWlaQ3A5ZnZnN3JiNGd3a1lqdUp891LzsOhHrkgsBvWCwgPbs00bH30zbZK38lr92Y0ZuUA=',
#     'MTU5MjU2MDcwMXxhTWI2QTZDSExGbW5tNGYxWkYzSjVaZWppeG95emFUVnBXczRiaGhjeDF5NlExM0JzNmM0RmN3ZEN2Nm41N0RRS3AzbkVFLW1ka0M0dG1kMzR6LWliem1yNFZBb2pzdDF8T7RAMy9w4Hr6WR1Xu6PJOdwPYwDAYjWBJpYaUpQzXbs=',
#     'MTU5MjU2MDcwMnxsNUd2ZU1YaHpidkdvWC1GQmVaOHQ0cjU5VExZck5jTEF5RHM0VHpUTTJpSVM4cnFNbFNFU0xldC1QQllwSG9yNVF6cWR1OGpDX01KZzJyWF9TbUNPNFlCYkRIRUwwdmh8958WWNvF37w70Kll9hm5oRzehfl659_Xgo0saLNoAWg=',
#     'MTU5MjU2MDcwM3xVajJ1NEVHOUwxSnFzYmNiR0kxQTNiNXhJOE9iV0NaaW41UnF4Zm81TkZiTVMwYTRTalJzdlIxRDVGTzE0NVR3QXpkUmlrdkp4UWd1YnF0UUVleE55LVBTVUk5YmJGeTF8Oh0ebHa8eTuZN0UVd30mUyty80OUxnTkn3e1zzJvtxk=',
#     'MTU5MjU2MDcwNHwydzI3RjBObGtCQmRkOGJSMk5ZT1Y0M3FfNC1nX0p4LU0tZUlTNE11a3plRWlhTVhMUlR0cXR1SGdiM29EV3QwNEdFZ3ZseHhNaW16ZHB5RE8wakI5WXZ6WUVWZmdnc1l8Tizt00jMzpEmKv9MQB2wK68h_GsNjGhoL4WKLpFVSBk=',
#     'MTU5MjU2MDcwNXxpYUhmZTB4QlFZdzl6X09YcDZCODN5eXVNSm4xdXEzbEdlQWlIYnNfSk9GUFJNRF9LS3lvdU1JSW1KbTRoOUNTTjJWMUstb1FMNm92Z3BxVGluR0owTXpIMXlFblBZQjV8_VyR6_eV_KMKNX-tazEfhGv_WPCJqryNm2Wn-tpcy8E=',
#     'MTU5MjU2MDcwNXxRY28xY2xyNWxlQl92bW9oSnV0bGpXUUxGTURkMDQ3ZHdGRTlaRmY1bGRfbnd4QmJaZlUybGZ6M0U3enVReGFpaV9lZG1Oei11NlZXUFpHUm1wSUVKWldUcTZoUHhVYXZ89iE9V2zKLls2pfhjDgWfo4TPQZ9GxSdfmKvuWt6wQ9A=',
#     'MTU5MjU2MDcwNnx2Q2RBYjNMd21Hb2h5ZUVadjNEX1JMVnlJNkc3WV9TVVpHbXJhVGFXQ0dnNHF5Q28wMmJvbi1NdE1uOTk0T29ob09oMlJqT0RKT2RzNFcwQWl1Y1BBbm80bUlPeHJfTTR8RMTncolXgm1dAeEROrHzmX8mbcs28eMHE-xzrJARFME=',
#     'MTU5MjU2MDcwN3w4bnZpYWs4TnMyellNYWlWV2Y1X3lISk9IdUhsS3dNd2RFVkxJUVZPb0pkajNXbWN0WWVSd2RkR1huNG9GRmdyd3U4R1hIdVd4XzVhM25sVTItcjNMUVRHSmJabklhSnJ8DRijL-uX8Sg9h5m_UR6VEYd7maktL6KK1kjSKupqtyk=',
#     'MTU5MjU2MDcwN3xlX29YZlNhanZ0TkNoVV93azBPODYwaWQzanhXNnZ1TnhNYm0yUDFMeWRYQUdWQ25UQWJTNWlheklXWi1jVHJXNDV0RkhsY2EyMFBYMjFOaXduVmczcjc1dS03ejU3OTJ87bV93VMvHRglaUDsLtOqh6BWcLO4UEUbZ9SwTS8kV3s=',
#     'MTU5MjU2MDcwOHxacGRranFXYURiQ2RSd1JUV3l4R2J1bi1RTi1JX2lpY3lsVU5OUFBWQV9ZbUVsUm95b1RNd2tuekhjazd4Y1R6Uk1qZ1ByaUVrUlp6Y21oc0d0QnpRM0dPaXk5SExoMzZ8kIzzceeMFD8f_7rQoVd6wkI9xHmJGv_ig6Fq9UKHv90=',
#     'MTU5MjU2MDcwOXxjaHJGTmQ0VUgtSE1vSTk0dUJqd2FROF9fYjJzQlFSYjRlRmU5dm5xQkUteFZsR3loZHBtU08xcUNiWU81cEJMRmRhM2JmTzc1SktkZ3BLeTVzVHl1cmF5V1h1aUxfV0Z8_4ojiLLT2b9DQUYhcAQp6SS2gtOjhReSG4snl8EjLlQ=',
#     'MTU5MjU2MDcwOXwxNFNNTV9pNk1FQ3VWWV9SZHVMQUN6N0lld3Z5XzZiNnRXRmFUU1FBS25BbUQ5MndsdXpGVUpSMG1hT1gwbm1nNUhhQ0xjSUxlWWJ3ZFh5R2hhQWZ0UGs2VkNMMXZoNFB8eRG_DuvdDY-CHXRluJAtLK5JKCQoSdQY3rpK2z2fGL4=',
#     'MTU5MjU2MDcxMHxJaHpIZWtfZEhEd2owNmNfblZRVlR6aXJENXF0NzVHdTJISk56VmV4OFRDX2VBaURRVXBpcHpMUlI5ZHhJbHlSeEtqZTJ5MmNsdDFzNlB1RmlPWFVDbXBBemRNWnZZZEh8lv66gK2bmaGZFyL7DVKgZbRhurYWoDUHhgrbcONzlGE=',
#     'MTU5MjU2MDcxMXxUcnpqMGFmbGpPanlfV2ttbDlJQ2lTbGozTFNmelVmRFhVRUFORXFFSTlIdG1teGxEYVkwTmhyRHh0NWx0VFlTSVF2c2VtYkxoWHNhMjg4SXZwVjhXOFNLT2xGYUdiRFl886dsKaMbPmkBi5hLaqZVKJEcWHpnBgKXYGhkPLq5MxU=',
#     'MTU5MjU2MDcxMXxKQlVYVk4yN0xCSVFWcVdERVJHeG1wSk1vSEFyODF3X05pdFk1Nklaeml0UDZjVm8zYlZaVFVXMFlaX0hrX0tmOU14dFptWmNQVzBnNmVuWThIMGJFanVrcU13Z1pRMmd8yLa9OO4kjKcyG5p0MWfhLn2DGgMDv3f4PUQZCwzGGqM=',
#     'MTU5MjU2MDcxMnx4V2t6aXdCN1U3b0xUTFZIaEFLcEpObWM3Q0R1OWNLak8tZm1vNDNDcU16eW9zQ2wxa3Q1Qi1kQWNTRmxTMGhMRW4ySVRkRDMwcHR4VVJwMjZIUkk5OW9CdnRKcjZQWXB8u8XEkwezFW2JyPWVmFFlnCfSGU2XhsEXzJ97X-fQVi0=',
#     'MTU5MjU2MDcxMnxWb0tCWnl1NzB0R3NwRk9WTUxQOS1DOVJJSFlrTEd5YndTVy1McWNKaXNrWlBpRU16WVNOb1Q1dnRiT2YzX2VIb3dmSUZic3czelBWQ3YzN3hqdzZGVDg5MkI2RU5hTGF8H50Oec-7g5kRLMLTMcD2q7qaCAozwCmnF_TG9I-sEQQ=',
#     'MTU5MjU2MDcxNHxxR0RiYjFoRjhOa0hBWEVZckFSYzN3Mkt1Y1ppcXh0S2ljczJJR0tMRXNqOVE2U0NFekF0TVNfOGE0VUk1eWpfNGRkNG1yM3Z6ZWlpQTA1TDJsV1NIb25kVXZuZUkxbmx8T3D7W-F9VG34YCktdh8UHkf6OScslbe8UUtW4lf-9NE=',
#     'MTU5MjU2MDcxNHxjbjhMYi0xZFhKYnczTDNtSWl4NzcxaXRpQTZmdGFjNlF2RTRMcUpoVlVReVJEVnRPYUw4cXIzMkI5cUFJVGxwREs5SGdxdnBXOW9xWWUtM2lPTWNvLUdKUnlBeW5vci18lagACUGWHUQoMNq-8Bx4DouzY6XucOrZNf0E-qRv9jA=',
#     'MTU5MjU2MDcxNXxZUk5hMVBzbHhmbmVxWi1OR0VuWE1FcTd3amN1ODNTR1RiNEUwU09ta3JpOFczaUp1M0VnelNuUmpSZXp0R19pMjA5ZUFHNEpZVU5CUkxVYzNhaWJrczR5bEFsSnBiaTF8mOFrxTF428iMZ5-vMWs40kAWrXkTWjuMtXVs_POuqyk=',
#     'MTU5MjU2MDcxNnxkdF96eW5hbE9yMnM3T0RUb0pVTnJIMG9RT1ZpWkRmV1pvRkdkMlptYTM3VnZjaXZONTFrbi1jN0JDNWNJd2FqWmw4akhlTEpIT0FIT08tUEdCSzl0Y2IzaUllcnNINEh8pWW2FqYq0IFRN_KLN20rRkiy-4NBV6-TXippuNXaMbE=',
#     'MTU5MjU2MDcxNnwtQUpLQU5yNWVOSk1wSnBSZTNlM05IdEdlM2lOUEZmZksxQXpLcTFYYTM1R2E3Yk82bTQ0SFI4cmd6QWdBVzZ0dmRRekFieFlIb0kxd3drbnA4RGlIT1M3R2s2aU5ING9822w2Ai62_9qjtG0Q20v7YDFZtzC0GDYK7arA-2GdmB4=',
#     'MTU5MjU2MDcxN3wyWDVjMlhBT0QzWHlmdm12aXZVZFpoelVEZHpLTUV2NWM1Zk1GT1lGNHAxbXFNVkhsS2RoMGpLcjZiYnpCRC04Y3g4WERYOEtiaE1wa19tc0hhZWU2ZWpQMDMzZm50THR8Vnj11P7_BODdu0MMrWZfvbENAk3KOSfdIXh4t3R_tP4=',
#     'MTU5MjU2MDcxN3wzRmRHREVFVEY2Uzkzb056bW16RTU3R3FmcFE0anZZZlFIYkh2enZLMU1nTW9hZk1vdWJkY0NqOWlzY1ZVc3JINDIzLVhOMkxweDM4V0ZIdjVWTWVjZW9OcVhpXzFaZXJ8F9sp_xghISWzK1TEdLEoeIN-5PbG0Tm7lcA16w-Ug5A=',
#     'MTU5MjU2MDcxOHxVX01ETV9OWVZwVTRubUlTaDJ6eXZoOGRsd2FtWVB0ZWY2VThNN2dQNFpBRHlmSzZTcmdsQkJtVFF1U0drekpRMS00X3c1MnpZZFRjM0ROSzBqU01UYk96MVpKeXM0WDd8RPGZrXnH6WC13KKDaui7CTNFiDyYoauJs_A2k2ZFOns=',
#     'MTU5MjU2MDcxOXxtd2JEY29zdFJyaDlXb2FXSXVoYnRCYUFKZ1N5STdPY3BPZFZHWTNMblhqbWJ2RWljbldvbHRCSHEwd0JEeUdEV1psQ2o5VVEzOWRWaTNCTzRYQ3U0QUhiZlBnOW1rNXF8Z_nCHd4kfXuW71tTAKxHKm71vIULhA5ilLApswWJlSM=',
#     'MTU5MjU2MDcxOXxpWDJfMGR6Sk45TlhGVWxEWkJJaHYxeFk5Z003bGxlZU82RWtneGRnYTNka1dWR3lHb3BBSGEzVFU2V3RqRjVseER3dXJiVlk0Z2tWUVAtRzlpT1JicENpcHBLWXFtbEN8oGvii3jRU20ilS1vh_L_8mPiuTS4RzQhpMapYJaqQT0=',
#     'MTU5MjU2MDcyMHxQQ1lrV21DcXRqU3Fld0U3dVdMck5iZ0x5MVp1bEh6T0t0OTEtUzdnTkRXelBrRGNaZlgyTGFlVkUwbGZYUjZ1Wlc5M1J2WGRtcTl1ajRUZWE3aV9jYUR6X0pKcVJlMWF8xMhix-SolW2y8ZUHAmjVKTZEkCzp9DIEm7A8rfIt72Q=',
#     'MTU5MjU2MDcyMXxmelZqdGwzVG1nbFlRc1RVZU1WV3FIVTlMV2p0S1dyTk5ETTNGdHBFZExXTlhiRTFxQjQ3UnZqbG9fVDAtNFIzLWhyVFhrbFhTdWVsN29jOW93bEw1aDJfVVg4M2YwZGt8v2cI3DWQtLmvDlITkge2QjaoqxsR-YQ1R1pgQvsG1NM=',
#     'MTU5MjU2MDcyMXxFeG9lYnhiWTVsbmVfVzlwWWFLMkUxVTBaRkNOS1dzcmZaTEhBcG03YjZQMEtsMmh1TWRwWlA5OUlxMVNJb2t1eDFlTVI1R29kajFIQTNzU1czMDlXZ0U1Zm1jdFh5QkF8QaAl4jFRLKb3f7VDXjqnZBavneS2e3PIZp2jOVqnecU=',
#     'MTU5MjU2MDcyMnxfS2lFUjFfMHo4UkpjeHhERXgzNUdOaWpBNGdaS1UwQ3VKaUpBTUV0Nk9ZZmpGRldhYXlWUmVYOWpKMnBrazkwY2xCRWpKOGRiNFdUakhOcHltZkkzNXVyeFUxeUxuVFh8kXDs24Cbv9sz_mL1jcXywpk6Gju3zJi8l6rhptmvtGI=',
#     'MTU5MjU3NDE0MXxvUDdKZUFKOFNiWFZaWnJfZFNkb0VlUHF0dXRQb3dWSENvZkZ5ZTZZOHQwM3QyNHBYXzNrTEhtMWI0MGgxRVh6RERGT0cxblE0d0hlNkQweUt6T0RTSC1aS3M5OUs2VU986I9txbJr-X7_VYiCrxK218MIBViK1lD-x_pyMaZMBUw=',
#     'MTU5MjU3NDE0MnxEUzk1Tm1VMkpvQXJkemczU0o1WlBTMzEyNFh6VUZYMExYZlE5cHlSSmI2VkxhNktXZkJEeEpENnBSd0ROZDJYZTZhSDJVcGdEVnBJX3pIOC11VWZkdlVmN2lySEJHb3J8XcWh-SXub2OzuVucyzf-FJ1kXuF_sYQl4bGRtiZa3Kw=']

# 获取client_id，由于为实时获取，因此不需要传入列表中，获取到直接发送给join_lounge
clientid_list = []
a = 0
while a < len(uid_list):
    # 获取获取client_id
    list = get_client_id.get_clientid(uid_list[a])
    # 返回值为列表，取值
    clientid = list[0]
    clientid_list.insert(a, clientid)
    room_id = '5748d744-b47e-11ea-9bcc-5254009bf4c3'
    token_list_new = 'poke_session_id=' + token_list[a]
    join_lounge.JoinLonunge(clientid, room_id, token_list_new)
    a += 1
print(clientid_list)








