from text_generation import InferenceAPIClient

client = InferenceAPIClient("OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5")


def ask_bot(ctx: str, q: str, max_tokens=200):
    complete_answer = ""
    prompt = f"{('<|context|>' + ctx + '<|endoftext|>') if ctx else ''}<|prompter|> {q}<|endoftext|><|assistant|>"

    for response in client.generate_stream(prompt, max_new_tokens=max_tokens):
        complete_answer += response.token.text

    return complete_answer.strip('<|endoftext|>')
