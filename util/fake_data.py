fake_flex_response = """{"result":{
"type": "flex",
"title": "FLEX",
"content" : {
           "type": "bubble",
            "direction": "ltr",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "Header text"
                    }
                ]
            },
            "hero": {
                "type": "image",
                "url": "https://i.ibb.co/NnVHVx5/music-and-multimedia.png",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
                "action": {"type": "uri", "uri": "http://example.com", "label": "label"}
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "hello"
                    },
                    {
                        "type": "text",
                        "text": "world"
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "Footer text"
                    }
                ]
            },
            "styles": {
                "header": {
                    "backgroundColor": "#00ffff"
                }
            }
        }
}
}
"""

fake_flex_response2 = """{
"result":{
"type":"flex",
"title":"FLEX",
"content":{
"type":"bubble",
"hero":{
"type":"image",
"url":"https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
"size":"full",
"aspectRatio":"20:13",
"aspectMode":"cover",
"action":{
"type":"uri",
"uri":"http://linecorp.com/"
}
},
"body":{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"text",
"text":"Brown Cafe",
"weight":"bold",
"size":"xl"
},
{
"type":"box",
"layout":"baseline",
"margin":"md",
"contents":[
{
"type":"icon",
"size":"sm",
"url":"https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
},
{
"type":"icon",
"size":"sm",
"url":"https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
},
{
"type":"icon",
"size":"sm",
"url":"https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
},
{
"type":"icon",
"size":"sm",
"url":"https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
},
{
"type":"icon",
"size":"sm",
"url":"https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
},
{
"type":"text",
"text":"4.0",
"size":"sm",
"color":"#999999",
"margin":"md",
"flex":0
}
]
},
{
"type":"box",
"layout":"vertical",
"margin":"lg",
"spacing":"sm",
"contents":[
{
"type":"box",
"layout":"baseline",
"spacing":"sm",
"contents":[
{
"type":"text",
"text":"Place",
"color":"#aaaaaa",
"size":"sm",
"flex":1
},
{
"type":"text",
"text":"Miraina Tower, 4-1-6 Shinjuku, Tokyo",
"wrap":true,
"color":"#666666",
"size":"sm",
"flex":5
}
]
},
{
"type":"box",
"layout":"baseline",
"spacing":"sm",
"contents":[
{
"type":"text",
"text":"Time",
"color":"#aaaaaa",
"size":"sm",
"flex":1
},
{
"type":"text",
"text":"10:00 - 23:00",
"wrap":true,
"color":"#666666",
"size":"sm",
"flex":5
}
]
}
]
}
]
},
"footer":{
"type":"box",
"layout":"vertical",
"spacing":"sm",
"contents":[
{
"type":"button",
"style":"link",
"height":"sm",
"action":{
"type":"uri",
"label":"CALL",
"uri":"https://linecorp.com"
}
},
{
"type":"button",
"style":"link",
"height":"sm",
"action":{
"type":"uri",
"label":"WEBSITE",
"uri":"https://linecorp.com"
}
},
{
"type":"spacer",
"size":"sm"
}
],
"flex":0
}
}
}
}"""

fake_camera_response = """{
  "result": {
    "type": "button",
    "title": "請輸入店家名稱",
    "buttons": [
      {
        "title": "camera",
        "value": "天使消費科技",
        "type": "camera"
      },
      {
        "title": "camera_roll",
        "value": "天使詐騙集團",
        "type": "camera_roll"
      }
    ]
  }
}"""

fake_carousel_response = """{
  "result": {
    "type": "carousel",
    "columns": [
      {
        "title": "title1",
        "text": "text1",
        "thumbnail_image_url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
        "buttons": [
          {
            "title": "text",
            "type": "text"
          },
          {
            "title": "post_back",
            "type": "post_back",
            "value": "data"
          }
        ]
      },
      {
        "title": "title2",
        "text": "text2",
        "thumbnail_image_url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
        "buttons": [
          {
            "title": "text",
            "type": "text"
          },
          {
            "title": "post_back",
            "type": "post_back",
            "value": "data"
          }
        ]
      },
      {
        "title": "title3",
        "text": "text3",
        "thumbnail_image_url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
        "buttons": [
          {
            "title": "text",
            "type": "text"
          },
          {
            "title": "post_back",
            "type": "post_back",
            "value": "data"
          }
        ]
      }
    ]
  }
}"""

fake_button_response = """{
  "result": {
    "type": "button",
    "title": "業務小幫手",
    "text":"請問有什麼可以替您效勞的",
    "buttons": [
      {
        "title": "業務後台",
        "type": "uri",
        "uri":"http://app.angelsctek.com:8081"
      },
      {
        "title": "沒事",
        "type": "sticker",
        "package_id":"11539",
        "sticker_id":"52114121"
      }
    ],
    "answer_type": "text"
  }
}"""

fake_text_with_quick_reply_response = """{
  "result": {
    "type": "text",
    "title": "quick reply",
    "text":"請問有什麼可以替您效勞的",
    "quick_buttons": [
        {
            "title": "text",
            "type": "text"
        },     
        {
            "title": "post_back",
            "type": "post_back",
            "value": "data"
        },
          {
            "title": "text1",
            "type": "text"
        },
          {
            "title": "text2",
            "type": "text"
        }
    ],
    "answer_type": "text"
  }
}"""
