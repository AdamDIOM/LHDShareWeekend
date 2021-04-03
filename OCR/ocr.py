import requests


def ocr_space_file(filename, overlay=False, api_key='helloworld', language='eng'):
    """ OCR.space API request with local file.
        Python3.5 - not tested on 2.7
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r#.content.decode()


# Use examples:
test_file = ocr_space_file(filename='example_image.png', language='pol')
print(test_file.json()['ParsedResults'][0]['ParsedText'])

data = test_file.json()['ParsedResults'][0]['ParsedText']

splitdata = data.split('\r\n')
#print(splitdata)
found = False

for line in splitdata:
    if 'email' in line:
        found = True
if found:
    print("found email")
else:
    print("no email")
