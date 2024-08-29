#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2024/8/29 14:32
# @Author : sunwenxiao
# @File : follow_user.py
# @Software: PyCharm
import requests

# 给用户批量加粉丝

user_uid = ['u1829060952460177408', 'u1829060954939011072', 'u1829060957443010560', 'u1829060959867318272',
            'u1829060962132242432', 'u1829060964468469760', 'u1829060967136047104', 'u1829060969530994688',
            'u1829060972529922048', 'u1829060974882926592', 'u1829060977164627968', 'u1829060979920285696',
            'u1829060983636439040', 'u1829060986480177152', 'u1829060988694769664', 'u1829060991286849536',
            'u1829060993962815488', 'u1829060996353568768', 'u1829060998601715712', 'u1829061000862445568',
            'u1829061003186089984', 'u1829061005694283776', 'u1829061008118591488', 'u1829061010857472000',
            'u1829061013487300608', 'u1829061016255541248', 'u1829061018835038208', 'u1829061021125128192',
            'u1829061023679459328', 'u1829061025935994880', 'u1829061028188336128', 'u1829061030402928640',
            'u1829061032688824320', 'u1829061034928582656', 'u1829061037155758080', 'u1829061039504568320',
            'u1829061041714966528', 'u1829061044156051456', 'u1829061046450335744', 'u1829061048664928256',
            'u1829061050896297984', 'u1829061053157027840', 'u1829061055883325440', 'u1829061058408296448',
            'u1829061060606111744', 'u1829061063252717568', 'u1829061065526030336', 'u1829061067749011456',
            'u1829061069992964096', 'u1829061072396300288', 'u1829061074610892800', 'u1829061076875816960',
            'u1829061079170101248', 'u1829061081573437440', 'u1829061083884498944', 'u1829061087026032640',
            'u1829061089878159360', 'u1829061092298272768', 'u1829061094651277312', 'u1829061097142693888',
            'u1829061099671859200', 'u1829061101978726400', 'u1829061104247844864', 'u1829061106806370304',
            'u1829061109201317888', 'u1829061111801786368', 'u1829061114226094080', 'u1829061116541349888',
            'u1829061119066320896', 'u1829061121717121024', 'u1829061124380504064', 'u1829061126821588992',
            'u1829061129237508096', 'u1829061131552763904', 'u1829061133851242496', 'u1829061136250384384',
            'u1829061138574028800', 'u1829061140910256128', 'u1829061143296815104', 'u1829061145612070912',
            'u1829061148002824192', 'u1829061150364217344', 'u1829061152662695936', 'u1829061155212832768',
            'u1829061157532282880', 'u1829061164364804096', 'u1829061166617145344', 'u1829061168840126464',
            'u1829061171105050624', 'u1829061173416112128', 'u1829061175660064768', 'u1829061177950154752',
            'u1829061180189913088', 'u1829061182391922688', 'u1829061184631681024', 'u1829061186951131136',
            'u1829061189891338240', 'u1829061192152068096', 'u1829061195130023936', 'u1829061197613051904']
user_token_list = [
    'MTcyNDkxNzA4OHxUQ1lfNGxkc3JWXzRYVFJtaXRxVVh2Ni1CdWFJSjlpWDF5ZkE2MzVBYzF2RHozbjN5UDZpVGdleWp1ZEFjbjFXZEJLWUpZbUJXb2k4ZHBVMEg3M0IxZ01iTnBmMHlscUl88bVExrVtDFsG7JicqzGZ7qnAsdu-CpV2JW9n8sCWQXg=',
    'MTcyNDkxNzA4OHxYdW9ZSjc2X1oxVDczNXZ1WUZqR2p3aGJoWlE1R2JXRDkyQ05JdWlGQkQxTEplWHVncnBBU2V3ZUlZOVpqOGphang5YzY0WXU0WUQxdVI4X21HZ09QSy1GRmV4WXc2Tl985uTbhARHnANIg_VoyDQpujg24wE1XYAB0On9o2kV6bQ=',
    'MTcyNDkxNzA4OXxVeU9OdHVhVUd1eHRzYWlvTVZhS2E0bEFFcXJaT2c1STFxVlN3cFlfMmdCYmZ3aDNQV1FMWUk2bVN3Q20wdXYwRElzclZTU0c0cnRPSWs5Zm82VmlNWTlSTzZXYnhjdC18394030kObaCY5aelEGrZjvWTYOtruMovhvDRr2eqVKM=',
    'MTcyNDkxNzA4OXxWTUVNM29jRUFMVmlDZ09aSUpzVTZLYjhjM0w1T0hmdU9VVGdtVmF5aHY3Y1N0SnBIcEpwdVg0cXFObjlBWGJvYjFJLVVHR0syVXV5V0NDVkJ0aG8zRUxXV1djbXhyQ3d8mdX6GRdYkeMXmPLE32wHmxn4jysvPGXPIt2uARzEzDY=',
    'MTcyNDkxNzA5MHxPSHlXajhZN1NBamNRSTRVZUxVWVZYVll2X2dvMmh3UnYwN1dmS1ZjdXRwRk4zT2xqX2lYemlxak85NG1hLVE4RHZsQ0NXMmFnOTdZTGZiM05jTUxMdnlRWjZuaXdmZ1l8oBnVNay9FCVQrKgcB3xswEvkLj4Fv2u-6SZVjkPPnBc=',
    'MTcyNDkxNzA5MHxWN2ZJZ3FRejlIaHZYbFJlZkNyUFhVYm5UTkI1eVlfQWJ3Q1l4RUs3bUszWUxnTzEza2I1cXNVUlBPMjlWdXhJb0FtVUtNU3E1OVhuMGQxZHF6Z2JrenpMZWpEbllaMC18UUwPygg-5bgv8-nupBZGrILQ-FYAAtXTBABttGd7W8k=',
    'MTcyNDkxNzA5MXxCUURhVHBfM3MzUkxQSXNCdFQtNm1pM1hFM3V0c0RhTmpzMjBSR3N2RUpqdmRiNF9YVFdYV1N1VWZ0Y19pOFdCcEN6ZWlwQ2I2eVd0czRLOFo4SmdvVE0zc2JhdkQ4dzR8QRwknXPlh2WONRpyJqJFxBbPICC5ESm1nlJQp-0dJ8U=',
    'MTcyNDkxNzA5MnxLYklWNEhLVjJyc2FjMmNPVVZXdVRRRDlDZGNGcFhUZml2UUxUVURENV9IaVotWXdwMXhmeWNEdVZYVzJocjQzN1BoeEdkdVF4bmdvbUw1LUhZTDBSRlhFVnNPQnlESHV8u5IPKyZQsZ6pd6EwCtpMXcASr6F-To1QpI5ZMjlClu4=',
    'MTcyNDkxNzA5MnwteUZudlZqMDZwV1c5Z3hLc2RxMWFtYl9aaXRNR3EzM1I1a2JPYUdqOUpObzFDdmtuRmI3RlB1RXJIenhKQzBWblQzdS16d1lqdGJTRk5ZY1RQbUstcXRreVFuWmFlSFB8g9E52HmgTl8LawoQnDAydzTrESbLWVu8ZaBEPI09uS4=',
    'MTcyNDkxNzA5M3w5ajJ2cWM4cDc5UzFrU0RJOVh3M3VmdDRVdVVyUGVxWjVRaUMzd0FiQlY5dmd1TjFjMExkSGJ4ZURIbGNyNzFvT1lMcEJzYzZheE1Dak5mV0FXY1BEc01ocklseXF0Sk98S3WHJKtCOQpcvSoGbkXgS9o45ayi6hphSGFRYPi3-Hk=',
    'MTcyNDkxNzA5M3w2RVhIb2dkdjZ5bUFkOV9LZFJrSkNPRlY1d0JXZE9vRlVra3F6UW5YalI1eDZ3NzluRUtBRUlPcXBiRnZzYWJFQVpUVDNzZm90UjhzWGJqNWt2N2hjUmZjQkoxTms0NG18SLy8lkJdfjvYvkHM_ZL79UXHxHJGraoEcFrLDtu413E=',
    'MTcyNDkxNzA5NHxrRDI2UDBmQ1laTElPLVpJWXZKejJIQ1QxOGgzSW0wUHdyRHJaY0JLeXRiV0UtVTU5eGI4dTBya05LazZPbHZONXM0T1lWemVqLWE1aVhsSHZEaWZEaEFyekpSOTFaWHl8-exXdmE2aKy3_dM3oAxZEIf8IqmCs9iwAxQz2_nnkdM=',
    'MTcyNDkxNzA5NXw4VnpQcFByQllGaXhLUmhjYUFWRGJKdVRsb3VvU1YxQjBEMC11WHJybkgyQmhvMFRnZG82NzgwVm42aXBDbnZKT3RBdVRIUjh3UzU3N1NEUG1MZ1ZzTTRxdU8wV3NwQnR8qMTWTI3-czChzzLY5tTpcnE9ULpbJeHVo_Gscdfa2HI=',
    'MTcyNDkxNzA5NnwwNFlTbkdWa2JFdjdNV2N2cVlfSkVfWmNLYURFbVZ6cjQxTWowLUtyUjNjcUk2WnE5d1ZlWG13bGRRaGpPTHh1RkN5V3prU21PQnR1QllsVEdpSENvRG9EM0ptc01jS3h8Js4jmHGnpGTkEpSbpvKtUwaYlOx1v86EgMcUAAPBTHg=',
    'MTcyNDkxNzA5NnxZeGhpZWNwd3NBRlEwM0d5NXBYZzVkV1FLanB2eGU4UUIzdHFJUk14NTUwREhjQ2RuYlRXeE44ZjhLQm55TU9MZFFhaThmbmZySXUtQWgxWThlbGJDUGxZSWw0MzN4VGt8WSnJL306YXe5f6kVAX54xsKhCtLfza8ZG-FQGPbxTJc=',
    'MTcyNDkxNzA5N3wxQk1FQmlRZ3dhelc2NzFsWWJhSnVKSlBveHk4VW5RZXh0bzUwWURFckpxdkJSaEdnMXU3bEwzeXk3b2JiRFJ3WkgxbWVsalBGdFBIQW50MjFnaWttbExQN1Nma0JHNWR89q4yg-GBpO0tlmYsm2ArHFQUm1gE7CwNdQEwl8MB3b0=',
    'MTcyNDkxNzA5N3wyZjVObFVUV2N0aktjQ2pCQ2ZiaDdhRzhiUmVQSnJ4X3NGMTJKc1ZaM2ltT2FWd1JxVThibkZDZW10R0lfOTcwcU5Ub3duTy1SNEFIbDRuTXp6RkxUUGM5MHBubTNhQ3B8BOw85gM9bYBq1DZ35-7L_02LSWa8OkzSxCTPa0jMSP4=',
    'MTcyNDkxNzA5OHxjUlZvdHZOMHNXUTlyUHhiLW5XZGQ5WDZ3N05lVENlSmhSMXhRR1V5YVJVYzkzaEtfdThuV1FwWHFIZHM5V29HZFI1VFdkVkprUmxvcnlKQVI1aEpOTW4xdGJQb25RbG9805JNF13h2VMh_qvpOyL5Z7609GQZr6oMmQCOR9HpW2M=',
    'MTcyNDkxNzA5OXxmU0Q2WDQ4Ykp3cVQ3U2I2ektwNVYyZEFtc3R2THdVdU1mcXhnZU1MNEc1UGg4Y0hSVVUwLUhSajlTMFFXek5wX1hlR2FaYzMwbi1aV3ZicE5pUnpNY0gxUXdKRFVCX2x8JdXuNwqFqoa3wyWA6mkJzUzBh0hTp9EUN9bxxznai9U=',
    'MTcyNDkxNzA5OXwwSElmZlBwNGhvZjFCOHAyX1pEWnpQaVBBeDVYQlhTV2xMUWVWUzJJbWdycDBwTmprclpIa01iUkRoUWhDQ0hrdmItWUIwTWlxUXdxMzdKQ0JFbWRxT0tUZE1iUmZMaEV8TvNl60DLukdIUCMYV5lwzF0mp0sraoyycfWUo1XbXb4=',
    'MTcyNDkxNzEwMHxrQzFJMEpRYkM0bV9BQlkyaFpsM3pWcUp2NzZzLWMzV3UtSzRrZkhIV0pDMlRtZkdyYm1pUXJkQV9MNWJ5T2xNVHFWeEFjTXlncWppTUM1M1NzbFotRTJMS05nM29Cc2p80mwMNym3gaxERXNqA_5vPWgXj8AYRfgxHSPKquZhyKc=',
    'MTcyNDkxNzEwMHwzemtGYmNmSVN2ckNTbHBZTi1iQkR5b2FiRWJyOGVlWGVPWkFOMzlhQVNxajBpdWFRYkFWZWlkdDh2Ul9kb0NsQzM0MENpSk1Td2NEd1k5V2V3bkQ0eWRhUVVMUmZaNFN8Y8w7zTVi7RW9ySfgm4U2K6wQULtPThNBKxmWllGu6Dw=',
    'MTcyNDkxNzEwMXxWVVFZY2FIYUREaXpSUVlDVVhiZVFpRGVsbkJKUEF6bkJOOTh5STUxYXZKR1hwNmRpZGUwdUlVNERzbGEtSDRMdnJ0OEhLUmNsTEtpRFJGUTdtamE4NW5tTDR2dG03WGl8c0ZJYfktTMLknW_8gWehjLLa3sTEJ05ZVvXgoQcPCoI=',
    'MTcyNDkxNzEwMXxKR1pXeFFkYjNMZWFwV0IweG1iQXlfR0gzLUlEVGVMRW1IWlNjdjVHMHdyT2xlajZUeXR3bS1oZ0JYU0IyYWVBZ0ZSTzUwZUdRejdOMFIxcFAtdkpWbk93ZGhvcVMtRXh8dZNErv98q5FibMJBNfCuizyZ0BkShERP9L24SXTEI6s=',
    'MTcyNDkxNzEwMnxLU0pKaGRHX2p5YjVMWnlPeVlyVHVaVjRBX1p6a3h2Z05CRFNZRHNHdDFmTmpxVkcwY2R1ZG1PUEZvM3NSejR4cVNkVHAtWjFjWVE1Z1BnSmtvWlBrNzBxWGJjNkFKRXN8vgXK83juF3Xmw-2GHLQ1tCTWvi3qb16fbQvyW8pLCFE=',
    'MTcyNDkxNzEwM3xJR0J3VzlMRHRtNXl5cUFyQU5UYmpFQ09MdGxNZ3JMalZHRy1rSDRreEY4S2xHczhTMVF0bzIxZENmOUVETnRucS0ya29KeHVSZDlsQ3hXTE11QVZmNG1ZSEd5Z0t0ZUV88dTJ5N9ArHNvdkeG0mfx4k_Hr60Zh98YvPWY6KAt0sE=',
    'MTcyNDkxNzEwM3xDbGVrNXcyeUt5ZEJNdDlFb2M4bW9kb0JQbktUQXFtVXlRUFBLMGxKMkxScGZ3MjVxeW9xMWZzbHlFYjUwQV82NURzOWUxX0lsTXdKRVRpLWhQM08tRU5nalozaThPMUt80FXdLz5rT7EwjmYi895eDty3smKirK0DM7HUfsXlvCE=',
    'MTcyNDkxNzEwNHxIYmlLa2V0ODVfdkR3aWg2a01mMExfaV9RMFpqeDVqbG82Z2NheFplYmNyUjFFSU9BcVBHN0NCdC1ZYS00M2tqY18wV3JwNUU1TXE3UVd3bG8ydi1IWDdtdGVyWVUyV0V8b5i1rWyfCAXjTgCnCa8nlf89_eXoDUqRZtY8TKJj080=',
    'MTcyNDkxNzEwNXxpMk9rbFJKQ0Q1MzQ2bXZ6aDZidUEwSXhYV3llVzd4SGVlY3NLSEtCdi1WSXpYdGNFTFFjYVpWa2lESk1RUmNqa05iZXVOS2pqSVBjVW1vb2RnSmlKNHVVSFM4Ym5JOEl82B11AhZvCFu-F_qaYuRlNnEjFKmvAffVdEoiXEsNCpc=',
    'MTcyNDkxNzEwNXxnRU5iUDBIU2ZBSmNkNVZOV1JqeUp0aEFaR3FlZ0I1SEVvQnYzTk5ZdjhMdXBINFgtYmtQaDdaWVNILUVXU2VmWnlVRmNOdDlGUG13R2xnZ0lGNTZ0VV9jeGtPSWlVZ3V8C2JZYFilIS7CEVTg3sxKBeVYR_uOi8MAzzs1pVbxW8U=',
    'MTcyNDkxNzEwNnxYMTY3dk9YYU0zUXcwcExIQ29YWEU1ci1GSDBtd0ZnM3o2cURNaUVqZ0RneU92ZEFDOTlrUTRkOHdvd09oeWpvaWxPN3JmbVJJWXB5TXVFdWdXd3ZucVgzeC1zZ2I3MXd8orL4TqvnkDhwpoGw6WOSJ7X7Ibwu40bjrJ3zDfxS3hw=',
    'MTcyNDkxNzEwNnxWRjkxZ0wwQ2YwUW5nS0ZDVnA0UGFabW8tcjlpTVE0aVRoNFdKb3IzdElveFZOTS1uVkFfVGhxMFlSZG5rQjdYaEkycGtHZVI0M3EyTFRsOGlYQk8wRGZWU3RPTlFsS2t81szT-eQ3RVoVesMWr_Xk9zJZe-gTFIkaAmDk7BlBghE=',
    'MTcyNDkxNzEwN3xVcFpWbklnWGtXSUhwYU5pQ2pMQ2VrX0diVzM5a0x6ZkpaQlg0ZWFfSGFfSFpUWUZkRDZuTWFvVFdqMkdBVGNNWGFVX1pqSDFhSFFsUnBraUluZU5NZ3l0cmJHMmtNSU58VtSivgOg5uiEhWE8VedMhn1F2sPzOjCjsmYKWuos8M0=',
    'MTcyNDkxNzEwN3xoeENienNCSFZwaFdFVDFGQ29DeEE0Z0p3TW1oWllaaXVsbjhMUVlKY2lsTlY2aFdpVm5namYteUpIZWZ6d2ZNRnJZYmhUc0t0YWhCeFJmRHFXQVdMMm53bFZmUXZuNHJ8ErOjiWuCMewJL8seu0_u8uDnc6HdwLMxr-XH6JNOMSE=',
    'MTcyNDkxNzEwOHxleEk3bEU2X3NWN3k3Y08zZV9ZU3BYYnN5OUd3eEZhR1ljRUFaQWNkQVVSclJxT0F4NndBU09COFRGTzFTMlFoQVJSeDdXUjJlOWluX3hHeWsyUHY2VlZsRldDLTg2RHJ8_ZvqjX_AR4PzzGQLVmwgm-fLNSeMrqL3-hG90yiz-u4=',
    'MTcyNDkxNzEwOHxKMElQbVB1WkZpWWdGenJaY0xNaFZFRGZ0cHplYWctbFR3QkRWNG5nMm01T0ZRZnVaelRDNmM5bGhYOU5DTDNWSEJOWjQ3Z3otU3BWSEhoZzJfV2I4SVo0OWdOeG5aWk5878NnvuX2Ihe9S9Yx2YNh0pMaLkXlqqa2bSB8kbbfvh4=',
    'MTcyNDkxNzEwOXxxQmNtaHAyaElwN3cwQnYwemQwblJhNjJJa01pY2tSbmRubkp5NzA3LUhNSjNiNFBxQVhSWmFqODdBY281QlY1UmFrM0ZvTW5wOWV3Z2tSMEdvcWZnbGJfRjd6ZzRmOVF8tlRqqhEOoE_99PtR92BPm975ExGGus7V56_zKDqZvgQ=',
    'MTcyNDkxNzEwOXxxMEVZdjg1YmxwcXNsYVlqQl9ocW80VnQ3SHVjVWRCTHlGSkQycFFGR1VCTktuSHUyMkZPUkZlYWV1bktueXFXSzFVSFYwTWJkMmdpeXFNUVFBUDRWZGFUMTJ1cy1fTDJ8mKZ5dMYiaEWqNHTEqCjTsjs8I5_jxFvXqT3ps0qHDk8=',
    'MTcyNDkxNzExMHw2SXItcmhweGZ3MDB2dWZENHRBZjJaR0FBdklxcExWMzNKbVZfSExUMUxVT0wyN0cxX2lFZ1NyMHhFWnRaSldoUWR2THd3TFpnNWNOQ0FCbDU2YURacTJzZE9pd29jY3J8xL3V3o2VHxrxKZuE0M3KN1tWjBZHSoBiAS7y1QQKUhg=',
    'MTcyNDkxNzExMXxpOUNiVmRNNWFDM2JEbmJjbWFmcE1iRm1MLXA1YUdCMVVuamZtZFF1TS1aYmIwM0ZJM25EWVFJWVMtQVZ5U2F0U2ZSVXQ4WloxQi1JM19OUGRfY2ktdkJfWXQ2S0Q2TlB8AydoTZQgU_-qH_38845owVi97JH47qtkrMEULGWFO0c=',
    'MTcyNDkxNzExMXxoUUJOZW0xZ1NOalR1ZmFiWF90UTFyRVB4UXRnd3JrYUFXV1lheldIOGw1b0g3NDh4X0xZSkVDNkVjVmtlX3dqN1dZQjhOVFo5MEh5dnk2Mk1mVXBsRkZCcDNLRXRDa1V8Dq8EFHrooWZ0GkrPpf25dC4b210xGmfycJ_-y2sAYcw=',
    'MTcyNDkxNzExMnxRdlpQNnh5UTBOSzNPbHF4MkRrR3FoQzBqV3hSVS1hWWF6Q3JndFJEMmZhUnlCeFlBenloWVZPTEhuSFY1MS1xNVlPd1RJd3FLeVJqcUl6SEw5T295QU5UbUo5b1lsRE18OZizs3dYMjP-slDFAdEygxFmLEfjJVvMvip6Eg-HpT8=',
    'MTcyNDkxNzExMnxGWDhXWDg5UGV6d1ZISlhIbUUtdEVWZjVwVG9vTmV3RWtsdjR3TEIzT2dSQXhWbjZMazI1V1lsWlNvanlnem1aN1lTbnNwS01WRl9pUVNXV0pvTUpZaW1fTmZfWkFlWFV8L57JTu7lyW0rkRhAu1cn9k-d15s_g2vBrcm1jset8XU=',
    'MTcyNDkxNzExM3w4UHFLcmx4dFJxUnMxc3Y4VWVRZXVPRFpKTTNCcXU5Uy1JZWM4Qk9kUm9kRjJZY0xfZmVkTG1LbjlnOXJVTjJrVld5QXdGazhTaGJtbWkyN0diV01NRldXSjJ3THlnOWd8ehpnRYXsvraqrC5ItU1ANvcSdNQ_F25S1oAF99NOzFI=',
    'MTcyNDkxNzExM3xkX1JGZlhXcHJoeWNTeDRSTHdvN19NNlRfNTNjMzRFSXNJeFc3SUVHSVhnV0FVbldFN2hNVkRYQ1JXSTl5WTdYVlBZcXpRTHNQbXdUaEotRG9ZamNoVThfMTRoSWRkeDZ8ikMHMAKPMwUjzlO06jqMZgioisD4_v1ZduTv4FU8LLk=',
    'MTcyNDkxNzExNHxNdVRGQUxZMXNXeWVnYXpsalFLdjZYMEJYTTFUbGtvdkl3c3RzQ2dGTkpYSGhMcEtQVFdNY1JLLUt0OXhocDI0LVlueU5LXy1zWlpBZjBTamFoaTlsNFBmREpQeGR5bF98H-3-Px2d632vsOZqIgd36_FykDGhDV7C-Liyg9s38vo=',
    'MTcyNDkxNzExNXxuRVN6TjhPaFRTZ2labTBtYjVDRVZsTjdRZGtRRllXdXlhdXoyMDJsUFItTFBjSy1kNFMxQVJzVmJZUktFM3M4Qlp4dnIxZzdTVEtubldjTGNEbFZRY09XNWlteFhFeXN8aCa-86_J_ui627EJS6fgukr3MmGJ5kbY5CQ5f0CTnEQ=',
    'MTcyNDkxNzExNXxSRndmdzdreTBHRkVIRmZSRjJNWXZxUFZYNGRwTEYxVTA0NW5YWUduSDZLTUpSVjVtQWhfMmpEX044WXZFc25CTVlyNVE0WWRkZ0FoSTllVW15WXIwaVdpczdhNU40aUt8-Itf4hG_nqsSq93nMzs9q3mD_iL8j4Hfs3Yf0zx4_Sw=',
    'MTcyNDkxNzExNnxjV1MtOHZQbWhMUHdvU2U1T0xsMXdBUjNOZXRXQ3BVUjMwYVd6ZF9hV2s4cnFYU0tDdzcxb3FrMllCTzBSV2dWSzZIeFg4TXpCZDB1ck9JaHFLc19VN01faWpYekR3Rzd8ovPELIHBrZnQ6d4rWtzwxOqU93F3pJyRUZZryld6Mso=',
    'MTcyNDkxNzExNnxNLTB1eUV0aTlFMTRWcUxaSFN1OXdkU1U3eW1JZTJyaXZCT1RxMVFZdjBJa1BwVUF1MGgySktGSGJkd3dSM1dXWm13MzhpZUJBQUdzY3hhanRhczA4ZnZ5SE5jWlVzZlV8luzakTYeJhTunmBLzeSPKZgodbLviY5fag2e0Xt0uOg=',
    'MTcyNDkxNzExN3w4MWxDWW00anF4U2xZeHZlSDBuZTY5dnJyekUzcmtfTXhObTl0UFZvd3BqZjlRVm5VYWJPM0dOSVVzbzNTQ0Vfa2F5SXZ2R1lmN3ZqejJWb0FDbHppRkpoT0lxY2Z1ZHh8pnZRXepnml0uiBVqusFechT-Wx83ABYNBlZHF-OgYak=',
    'MTcyNDkxNzExN3xTM05jMXVZVEhMX3FDN0lQbzBvZmRtZmk1UGZSTjhfNjRyM2dQOUQ3U3FOMzBPSF9MZUI0VXlibGNxdmhSUTdSWVlrYzhqZ29ydDgxVV9wcUtWX2NLWWlnMUxkUXJvS0R8QsgWAKrNUhQFfgqhTMZB0IAkfZn_-9aedbLQbvVufN8=',
    'MTcyNDkxNzExOHw3b1BmR3o0YkJ3MmFHMFJBQjBLMkM5TnV2ajlwNFFZclFOcENpeHZaeTdMNHVMbnBjX3ZnRzFQOXlVeFJ3ZVRNaldXSmpiQTZLbFpDUWV6VTA4M0hRUWZjeVRfblY4M1h87Q9E1VRpgUnbi56Vqbr4YJgSX6RjwVYv5IR8G4rGRJ0=',
    'MTcyNDkxNzExOHxNSkVtOHFBbHBIVGdWVHR4UVZ0T1ZrT3VVMkVpUzI1Wmp3eE9kamVGbHNIMjBYRFBZZ0lYSlF5ZjFFU25sUkx6UzV3a1VqNVYteVN2amp5YVAwZnlnRmJueVI3SV9zRTZ8CbrmurPx402Pp1j7h2u2MCQFzjF-Mz6FQ2V1THLRKq0=',
    'MTcyNDkxNzExOXw0cmRzbER1bUFyMG00QzYwY0xucVRmUnRaeFVPYnNWRTRic2gwWmFnLXFBbGVBOUJxSEdtRlhfRW9WcTZIZUdGT3F4UU1xX01Gdkh0bXhzUWtRNkNsMkd0Y25VTGNjaUN8MFM9h5kvuid_UuKjZrQPZjqKtAQvkKmX5uO5JeUxpJg=',
    'MTcyNDkxNzEyMHxKSXE2Tkh0VGRuUHlPNjhBWml6bE5YZUt6MWw5dlg2Q2dZa2hvUFFaeEgyZi1jb2g1ZXBZSGlpUXBqclhfZk1veTNOLVg0cjRSdmNod05ROWM1RHpBWTBpWXNGcXRIZ1p86KnAcmcyxaonYpXnX8tTtfE6gW2TDED_SUru5tb6jYs=',
    'MTcyNDkxNzEyMHxaVUVLSkF1UlJQaERNN1hOczN3cVNQV29VYWNNbm9lc2JfYW5uYU8yTFU1TlgweXhtTnE1ekFlbVY4TmNaWmJrMmJocUlIQ1pMbDV1ZGdYNDVjVmVEdjNqUlBDQlcxdnl8xPLEpTQ8mZQtXW38XDYRXJMoq3PU2RDDzEwuxVN09z8=',
    'MTcyNDkxNzEyMXxMVkdiVkYtdWx0OXpEWG91Z3U3NmZjMkNJV3hCeW1HNVlpMUY3Z3FlVWRaRU5sUTBtYnZDX3Y3ZlBxNk0yUHFoZ0J3ZkY0V1B6dUxuX3N5Mm1aM1ZZSWdsNUFtRWczNTJ8b66ANQHOgCf9uvRZrse4YoyPOFdALluU4-GIfqbkbRI=',
    'MTcyNDkxNzEyMXxpczhOX0hzMi13clVvODI3c2o5OGlwWUtUNVBZSjh0VmhxbUdrUlRNaTJvVjFhV0NkTE9PdldlRmR3Y3dOa3dqdGdhYzJrdXBMY21hMXVuMXNBWXpSbnJTYUxiVDJnSEJ8HqHz34fNO_l0KDms0gUcmHco7gPL4H6L-2N1uDapVeI=',
    'MTcyNDkxNzEyMnxySTZEX0ZaQ3l1WkJQc1RQY000NzZuQ3RCREFFWTI1cld3T05tc1VxWlJWZXZzTzNiRFFtRXl0ZFZXOWxpbk0xOV9OdTltdDd5ZlhnZngtNWg5bnZiTkpIeWpiUWhiZHB8WcFAbGbH1uEEj7QA7XzIuxPROyhRtcpYbL846alGCVQ=',
    'MTcyNDkxNzEyM3xXZXNQc2h4ZE1sNG9NV0FJQmFHZVYxczJzOTUtMjN1VHcwbFlTY3BWUzN3LWlDLWVpVVdBZnBGVXdsc25nNzI5Yk5CSXA5NDUycjJMVU1nSGdEOWZrcV94SlVVSW1nS3F8lJmlz3qWOUGrb7-hkO6gL0quDnn1che_iyf0o-Jv7YM=',
    'MTcyNDkxNzEyM3xIRFo4T1BiWmNOX3A5QzJJdE05Ujlnc18zOEwyUERCejJlU3NNSUFud1d4Snc2bXlFaS00TVc0ZzZ0YnBDaWFBS0NmLUlnci1HZ1VxcmR3ekFESWoxQ0RVOTFNdlJzWGF8jHzU2ru72gD6u6cyKhSqCzv6n9UFIgnJI_XSzL88xNQ=',
    'MTcyNDkxNzEyNHxwUkZmcEpQbzZkMXBxYWl5cmR6UGlqTW5HdGd3U1JLOVUwNWs3QmxjdlNmUFdKTkF6dHBubXI0NW44bkZLN2FXVWtrZTA5RC1UdHp4aW1MUEFLZEdITGpPVFd0aWFkZ0R8OKK6UMNL78dj8vVl2GLnC-YvUpYomPOk-ApI8LZQWoI=',
    'MTcyNDkxNzEyNHwxVzVWMU14bllGU1FVV3M3Z3RpWUVqMi10bTZUbzRxVW8xT1UtUEl5dGRkcmNXaU0tcW1IYWFYNnFTa2tHRHB3N1RMRnVqTXpiT3pfZW81cEtqeUhXbTFnTWhBOUhGLXJ8RdRWBtJ1u0SgdCDziPTv-1x0yOW1ADvv_C3wVHuasYE=',
    'MTcyNDkxNzEyNXwyOExCS1ZPRzdBeWU0NnpWWTJBSnBpaVVxRGZuTEwyTUZVZ2tQU1p0blo3b3p4aU5vZXozaG1PMWEtblIta21wSzZCSHB6MjF2RVlyRkE1OU10WUZfTENFaWF6azJCZEZ8xorJNTWJC8lX2QXdxSSenEmzYHWHpMxd4Q6qIB7HLtM=',
    'MTcyNDkxNzEyNnxzdzFST3lJaEJtOXdfM0trTEpVdHBiMDdvTkdtNEtzQ2wtWHdIQlJtbGpCbmFlMW9TSHVDUGZ4REVrWVNXYUVvU3NGY1ctNGpud3pSenl0enFEZkUtUXlzMm9CQjAwUmJ8k3wN23qxXk5rzFdERKDnhuUKOl6HUpqSf_I6Y0kibQY=',
    'MTcyNDkxNzEyNnxDUmlNbFViWEZXUXM2RVBvN20xZzZlUWpUUXdybDJHVzFSallYXzdTY2szRTNtZVVtSERzNUU5UVJXLTlBYlowOG41N1ZPZ3BNSnNJSkdSeHE5elg5Y2NNQlNTblpudzJ8iQKdlFTqEUP6jOUOjRpAvBYb_GvoSC_QqjNzfqdlZPk=',
    'MTcyNDkxNzEyN3w0cjRuOHVNVXVaOUw5QWtMbFZDcUJqSl80VG9fMXhidHAxYUk1bHRDc0VqTjlwOW5GVzZncTg2LUZKY0tIQjVKN2pTMFFqTFQxdjJja0loOUdScWQxX3Y3N21RamF6OFh8ETz_b3gpeImUXI6lDFiPSWtaP_mW1vUMwjOgl9_4hY0=',
    'MTcyNDkxNzEyN3xmbHRqRl9yUG5GYUxhVmo1Z2ExUVZEeXlGX290Tm94OVNmZlk4R0ZFVWF1cEU0UFRNdnlTMU5mb21RUmd1a21vSHF6NDl2SWNjakgwaDZwVk83UWNicERRUlY0eTBWUmJ8C3_EpU4cJ5KPj30BI0SbzY1SYP8kEfi-EAE3q2kydAs=',
    'MTcyNDkxNzEyOHxCOG1ia1NtZWtlaGN0VDBMZnVmQ2ROMHV5ZTZtNFlLNUJNWjROajk4bi1sN0lkSE9zNTlicUdjR09qc3k0SG92bjZ1N1FYMDFBZHpZdTVsOGlIbjVhQmRZY281RTFzSXh8QOl2BHwz2S17L_BzfHIoh96Y-FkF1jJDD_x-x1BXL7M=',
    'MTcyNDkxNzEyOXxsNmVvLVA1a0pSdWMzX2JBVlB4eXhQdGlTZVF6cVNYUWQya2hhS1ItRTJRSXdLSGF3WkZTdzdhbk1vajFmbmVsX2FTNWlYSWF3czlXUmNFcGt2bmEyUUdvMUlrQmNOUU58liGx3yGyxLoriKtpbl41ywJPJaRBuVSXWArOhwYWJts=',
    'MTcyNDkxNzEyOXxUcW9QOWp4TGZWaVRaU3NhSi1iSWtKSDRRZ1k4ZkpwTk00dVVEeG5YT1RyQTI3YnJXeGJiQkhlY1ZscmQ0SHVtSm1XeE50ZnZpWlFJWHp4SGdRNjhfalJyVHQ0eHNZeGd8bKNC1WTSL_WN6Kng8Sxt87EyFYZ9GnjnRrTpAVZksP8=',
    'MTcyNDkxNzEzMHxiMWZiQ1Q1RUE2YktFMHJ1ZXRCS3dzUkpWNFhzRUpFUV9PTmNxQ1V0dzVQbFViRjJsLWRWX0NoWnBvLWNTOGx5SF9DcmoxWEFEQUlvQ3dBOVprb2t5NkRHMW9Vbmxxc0F8DLN88xWw8hTRXrTJP1NsXyR1FAmGduFCkWUZ40EXkr8=',
    'MTcyNDkxNzEzMHxDY0I3MmRaZVYyeVZyU295TFFLaG9YRUlFVjhIei11OHhzUzM3UTBhWE5ZeUNrM1FDV1FBSFUxS2RnczctMkliaHRjZVRvMGNqSGNwR01nMnZ6OVFsNUpIRHpfbUEzZDR8J2Zb_8YnJMxZSQUoi3w8qkAnmTHKP4MXWP2Ktss6frA=',
    'MTcyNDkxNzEzMXwyd1NDNnFPd3B0aDlHYWNDbXFjdFN3QUhlT1JweWRoUndrX1VteEF5WG44M0l2aTdSajQwVEtYRnRWUmZzQllmVHNOcjQzSTRBb0lRRkJvemtPNmZ4UGFnZk5jeHFxNnR8et0ejIuK9fjJapEMyOqraolSoZP3qbxagbkOFFho19E=',
    'MTcyNDkxNzEzMXxhbTF5MlpESVJIeG5NbVU2OEo3d2xmQ294VnpCU0trYXhkb0FLb3cwX1JyZWlDY00tdjVyR3lfTE1SUDhrVzRudnFFSUd6NUlNM3RjMTdLZVpjeEZsQTlheVNSYklBSkV8k04FUqTfLIhflFwYdumNG3PAQa4Nh6R_BxNE3Om6lvQ=',
    'MTcyNDkxNzEzMnxyQVZma1FjZGVZdzdpeWVoQ3VoajRHYUV4UWp0X0h2VFdJVEZXMWJhQ2RRdV94NjR1OHpibmUwN3ZfQUI2cmVuN09Zbk15ZTliRDJDcFhfRkQ3QTdoNnBXR0RpYnctUEJ8Qc7yMS-LgdIsarffunSgFdiN2zeDMWjtFM1XQW1BCDk=',
    'MTcyNDkxNzEzMnwyeUs3eFZ5Nl9rTzN1TGVUMFhUT3BkZ2hYUS1UOF9oWUZTUzZ2WC0yUlpGQzl0QXUweWFERG15cGlNZVVmbWFGTXpfa3hPeWFTUGtsMXJnam45NU1VcTdUaEJtWWhPcUl8PdlL4o364BVgsU5-hVbvoNPq3CSzNamGydGE6LliXR0=',
    'MTcyNDkxNzEzM3x5NDdiQktjd1V4aWQyTVk1dmttakhUT3FHd3VWU3pwRmFwTnVNU3hHYVE4UU9qaW10dHVqeWpxV042OTBOVjBqd1ROc0JfZDE3bGpDZjJkRGFlcUEtY0NfNlJqbFRKZWN8FWGfNpBMcUWK1Vc9OgfQfRXrsDIQ3EaPqmTGBTZEgn8=',
    'MTcyNDkxNzEzNHxEeE1uNkJYcVRRNEw3YlNSWFJHZHdodVR2WTNfTFl6bUNPMFpQMFNfdmk4WWwyaWJCYmxSdVhiVDhPUF8zWXc4U0E5dWVMbGpONzNJQ0xibWNKWndUN3B1UHNYMDk4Vnd8pVE-pNaocU5kglDlgbsPD9GXjaJsFYADQvN8J97SFhE=',
    'MTcyNDkxNzEzNHxXQVdQNnBUbDdxSkFESVp5dEJtY3hRcTFTc0lKMWE3NXRhNzJueHFZdG52S24tQTk2R0VuTU5SSlhBcWxBMHFQMF96c3VfWmR1ak0zTEZPVWdPOGhwTm9KaUhwWU83dC18CovWGAuWe5IzXtu5CNyZCD7mtDF_H2Z3mifJPPjuldk=',
    'MTcyNDkxNzEzNXxCSzFHazAzSEo0Q3VJaWk5MFZYNWZmc3VZNTdQY1dRNWxGREk5RTlqV1FFMTNzU2o2RF9YR012UjBhbkdRS2dpMUdVV3ZVeXUyeTVISDZqdkNTMXJrMkRRWWQ0THBzYWV85yFmbFJOhPRHFvrsj4VaagnRjdTjRKHsDQFzHuH5XCY=',
    'MTcyNDkxNzEzNXx5S2pveUpTN3FVcXZWMFo0aV9naVo4ZC13LUNSVy10cXA4WEdXS3RNZ0ZDdno5LXhYY3FDdmVIZUNUaXRnSTNfSUhlbXkwSFk3N3F2Q255QWdBV0RjWTk4UzNwSlRmSHp8cZCXiQU1-z_bAdvN_JD9wN7fvXFAlw0b9ZUPUnZuPCo=',
    'MTcyNDkxNzEzNnxkRXZ2aXA0d1QzYXVxdkc4SGVuUEVkeVM2NXhTRXlnamt3Ni1ZX05TYzBLc0hxUkZuQ0d2cmZ1ZHhrN0RzWlNfdWN3ZVUzLVFTREVvMGlZUDBQM2ZHLXNqempJNUxYUk18WSbv8PNSD51lGY-qkRiUZ7QE6DMlGqiim4XupNQ7AtE=',
    'MTcyNDkxNzEzNnxibjEtMEN5OC0yc0ZleURHUDlCWjJQLUdha3lBVlpnNTJjenJmSWVtV0ZKbDNIUndTV0ZMcWpYUFlhZjFfaU91UU9mNEx0T0w2VGRtcTh5X3NGUThGWkVITnBzQ2hPaFJ84UOt0LzpxzgLzUoGDmYR9GaX5Y4bFPhnOTH5yOqJALI=',
    'MTcyNDkxNzEzOHxIV0gzRzkwNEgtaGc4ZVN4TTduRHJKYmE5ZkNnSFV3RUlsRC1IVHFhTldYbHRKcTJpdHl1ZUN3Z0I4RVRiZDExNUtlYjU1OUFveURZbi1fd2h3TlBqM2tCdVhyU2hJODV8H-9xMQi8CL08BO7C6r7SjU1OGfuICNHHGg7HlQkn4e8=',
    'MTcyNDkxNzEzOXw3Zl83NDNPc2xZX1RrWnBoVVBxSHdfVUlEdjhBR1RNQkVqLUtvYWktbXZwM1IwRVJBd041V0QxbVBmRjBTWFlwS2ZoNm9HVW54YmZWczRBdjFFRDdIQjV2TkhIemR2LUh8ZWoooz8mht5tq6wmvrFkHoIg2ductwh3exxvs03OMi8=',
    'MTcyNDkxNzEzOXxwLWduQzQ2NHJpYzBpbUJsS1ZBMi1tZmNmcTFLUk9idnVhU3BVc3BXelVpbGM3RUNTN2RhbjQ1N2V5eEhOSE16Z25jMU5YRzVKUnpxcUhoTmV3c2tQTU53WEVlUFFwYXh8HDfv13lUoJ-QlSXS89xKZja2XzsQdGuWoNgPki-AQrs=',
    'MTcyNDkxNzE0MHxjTUxzeGh0T2JjZ1hHalYzYVR1aU9PVm5fZXViUVZMRm4xdUxMMmk2VC1mUmxLT3NzRVgxNzRTN21MejV3V3QyYTJDSUJyYUxscU1HLVlVOTZ6NUpwSHNqdnIzUXlaNVh8A1KX0ytkQbDLcQ5dqEgg54mxAwoNayJ19ABpxHCQV0I=',
    'MTcyNDkxNzE0MHxJd3htVG1MMUJPdS1EVFJsNlUzLTJzX1pwZlJjXy12Sk5Wckh6cEVYY2c2bExDMHhkRHd4MThBbFBwczlJTF9OUEdvbUZBUlFvNWpCNmh6NlljdW5aNzRiSmdpNGV5TzB8OwZsQUqymw88_0nAJm3TwguHsxqdHfwZIlsZhTN9uHY=',
    'MTcyNDkxNzE0MXxseU53NUFDbDlGRjU4cFBkNV93MHMwMXpVbEtaUGIzZDlMV1Qtb1BDVk10dXh6RmdYc0tJNUoyU2QtV082T3AtMmFWQ1RVMnl3NUVOblZkeU9mbFlYSEhuYmwxVHE3MkJ8K8pPHPGTH4QSMaZpy506jSb1EHPrpAUDIhu71O_giHk=',
    'MTcyNDkxNzE0MXxLRGVoQ0E4TzRhRFVwekF0amdncWRjeDM0c21vSG9QZkZzMzJFdXNVSndWSVF2RHlLSlc3aFFkazk4Rldtc3hUZzd1bG9GWEVpeENuVEhuVDBlMU1vczlMeU5DTDd0Rl985IvOPQWBjoqrVL39X7ziwAmGE0N1imnif4_U5GrYNU4=',
    'MTcyNDkxNzE0MnxxMmJnaGFuRFAzV2w3VjV1blFCMmsxQlhyMElMZklySmJwTVU5b1JtN1ptOVQ0cmZ3WDJrRW8ya19DekZCTWh5Tk9tREU4a1NYVGVjTzV0c01tZVhxc1VNc3BnXy1kVFp8KpM3aCuTfTDEOdV8dwHpd5t4PABm5Wejqr892W54b8Q=',
    'MTcyNDkxNzE0MnxzcDZjOEJrN2dNN0pEM1ZyWDJ2SEFRZ2RFTU1UMkNmX0JDSWtLdFZ5cG1xVHhEZjBfVVl0UWg5UXpXR1NUeWh6WWxTY3pZZkpaTlExZ3dSc05sREJsaVRlYkkwWE5wX0Z8Wk9Qli7QyI9BpuZ-lWo07RRF-W6vhY47EKOpLjzSGQQ=',
    'MTcyNDkxNzE0M3xFLU1mcld0MEplR1VIWWxHNVNXNXhQNU5NSjJJUWRSRTVXbkVGU3hyTlI4Wnl4WUd5bE45TUNaeWd4SlBrc3lZeHROb3NnX3lIRlJTSDZUR0VicDFQcUQtQ3ZsblFRUHJ8vJuoVHENQePnpVs3xV2-SK-pinc_98aI_l3-ITSe3sI=',
    'MTcyNDkxNzE0M3xDa2NwcFYwZmxRNzNUeENjM0p0bFJJcm4xSkNEVTI3ejFjTVFZVnpPUXp6dUt2WmJIZ0F3SlA2X0h1anNkem1OZkdUdUxSTHNKZzFaVm9GSXdZQ1BXeTlTM0NHYzdLd2V8sUhlDwsctSyLKH7j22XF0NUSv1MSGR-aZgM3Vx5576o=',
    'MTcyNDkxNzE0NHxqQVpfck53eW5jYU9CUzhDLVBLREhtcEhUZ1pKWnVSTmtnclVyUXJKanhZLVV1OGI1djFrZFllandsRTZsYXBmcG9lSnM0UFlMLTIwTll1Rm9mdENIU2p3Mm5IMTRlYVd8fe8TSOTX9ZktdK7q8Yd8STD-FMSjaPRQGUtzzOUMjAY=',
    'MTcyNDkxNzE0NXxlek5wTTltSlZqQWV6QkJaOS10ZEhhSFhtZGZiNkVCZ0lVZVNEZDNnZGszV2dsdGpVd2prNU1jMU5wdmhKQWlOc1BwTmtia25jTnpuekJ5cl9rdkVnVmJudEpTcW1YN3J8jMtloNMe4tHhoLJOAN21miXEXfcdSdnEU8bxuOLyec4=',
    'MTcyNDkxNzE0NXxRRFVJLWE1QzlyWlZlVVBfWGFrcHBqZXhTMFFEc1ZzbHNiM2tYNVFFSHhIZ2d1bTdrNmRIVE8zYlE0QXVlb2oxVlJVWEF5eGxiTl9LVXR2d0hIT0pqa2F4V01pMjVwTHl8qoMHedYoFR3oCZrBDIYVTpuO8WtCeiDqcn22jmtMcpg=',
    'MTcyNDkxNzE0Nnxtd1BZRG1ZODVETHlrNklJbFdvdUh1S2FzYldla0tCRUxzTlFYSXEzYlNoOWxNWnkxRjlTUGZ4Q0FhZ1l1TXFOemRjbURETHhGYjBkY3c4dXRZV2ptSGJRSEVaT3VlS3l8Hm_QlzkiffyCTmJToMNCCpXqrBeq2-c-fYFtVDZyc3k=']


def posturl(user_token_full, to_uid):
    url = 'http://test.api.pokekara.com/api/user/relationship/follow'
    header = {'cookie': user_token_full}
    data = {'t_uid': to_uid}
    res = requests.post(url=url, headers=header, data=data)
    print(res.text)
    return res.text


for i in user_token_list:
    user_token_full = 'poke_session_id=' + i
    posturl(user_token_full, to_uid='u1738054920313843712')