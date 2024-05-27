import json
from langchain.llms import HuggingFaceTextGenInference
from langchain_core.language_models.llms import LLM


def load_json(path_to_json: str):
    with open(path_to_json, "r", encoding="utf-8") as f:
        resp = json.load(f)
    return resp


def load_llm(infer_url: str, temperature: float = 0.01, model: str = None) -> LLM:
    assert model in ["hf", "deepseek", "qwen"], "Invalid model."
    if model == "hf":
        return HuggingFaceTextGenInference(
            inference_server_url=infer_url,
            max_new_tokens=1024,
            temperature=temperature,
            repetition_penalty=1.03,
            seed=42,
            stop_sequences=[
                "\nNew_Question:",
                "\nQuestion:",
                "\nTable",
            ],
        )
    elif model == "deepseek":
        return ChatOpenAI(
            temperature=temperature,
            max_tokens=1024,
            verbose=True,
            openai_api_base="{}/v1".format(infer_url),
            openai_api_key="none",
            model_name="deepseek-coder-6.7b-instruct",
        )
    elif model == "qwen":
        return ChatOpenAI(
            openai_api_key="EMPTY",
            openai_api_base="{}/v1".format(infer_url),
            model_name="qwen1.5-14b-awq",
            max_tokens=1024,
            temperature=temperature,
        )
    else:
        return None
