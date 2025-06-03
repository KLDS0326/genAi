import boto3, json

print("\n----A basic call to the Converse API----\n")

session = boto3.Session()
bedrock = session.client(service_name='bedrock-runtime')

message_list = []

initial_message = {
    "role": "user",
    "content": [
        { "text": "오늘 하루 어떠셨나요?" } 
    ],
}

message_list.append(initial_message)

response = bedrock.converse(
    modelId="anthropic.claude-3-sonnet-20240229-v1:0",
    messages=message_list,
    inferenceConfig={
        "maxTokens": 2000,
        "temperature": 0
    },
)

response_message = response['output']['message']
print(json.dumps(response_message, indent=4, ensure_ascii=False))

print("\n----Alternating user and assistant messages----\n")

message_list.append(response_message)

print(json.dumps(message_list, indent=4, ensure_ascii=False))

print("\n----Including an image in a message----\n")

with open("image.webp", "rb") as image_file:
    image_bytes = image_file.read()

image_message = {
    "role": "user",
    "content": [
        { "text": "Image 1:" },
        {
            "image": {
                "format": "webp",
                "source": {
                    "bytes": image_bytes #base64 인코딩이 필요 없습니다!
                }
            }
        },
        { "text": "이미지를 설명해 주세요." }
    ],
}

message_list.append(image_message)

response = bedrock.converse(
    modelId="anthropic.claude-3-sonnet-20240229-v1:0",
    messages=message_list,
    inferenceConfig={
        "maxTokens": 2000,
        "temperature": 0
    },
)

response_message = response['output']['message']
print(json.dumps(response_message, indent=4, ensure_ascii=False))

message_list.append(response_message)

print("\n----Setting a system prompt----\n")

summary_message = {
    "role": "user",
    "content": [
        { "text": "지금까지의 대화를 요약해 주시겠습니까?" } 
    ],
}

message_list.append(summary_message)

response = bedrock.converse(
    modelId="anthropic.claude-3-sonnet-20240229-v1:0",
    system=[
        { "text": "모든 요청에 해적 스타일로 응답해 주세요." }
    ],
    messages=message_list,

    inferenceConfig={
        "maxTokens": 2000,
        "temperature": 0
    },
)

response_message = response['output']['message']
print(json.dumps(response_message, indent=4, ensure_ascii=False))

message_list.append(response_message)

print("\n----Getting response metadata and token counts----\n")

print("Stop Reason:", response['stopReason'])
print("Usage:", json.dumps(response['usage'], indent=4, ensure_ascii=False))

