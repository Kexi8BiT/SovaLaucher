import requests

def __translate(chat):
    systemPrompt = ''
    parts = []

    for turn in chat:
        if turn['role'] == "system":
            systemPrompt = turn['content']
            continue

        if turn['role'] == "user":
            if systemPrompt != "":
                parts.append("<s>[INST] <<SYS>>\n" + systemPrompt + "\n<</SYS>>\n\n" + turn['content'] + " [/INST]")
                systemPrompt = ""
            else:
                parts.append("<s>[INST] " + turn['content'] + " [/INST]")

        if turn['role'] == "assistant":
            parts.append(" " + turn['content'] + " </s>")

    return "".join(parts)

options = {
    'maxTokens': 400,
    'model': "meta/llama-2-70b-chat",
    'systemPrompt': "Your task is to identify unsafe images",
    'temperature': 0.75,
    'topP': 0.9
}

context = [
    {
        'role': "system",
        'content': options['systemPrompt']
    }
]
def run(prompt, image = None):
    context.append({
        'role': 'user',
        'content': prompt
    })

    body = options
    body['prompt'] = __translate(context)
    if image != None:
        body['image'] = image
        body['model'] = "yorickvp/llava-13b"

    response = requests.post("https://www.llama2.ai/api", json=body)
    result = response.text

    context.append({
        'role': 'assistant',
        'content': result
    })
    return result