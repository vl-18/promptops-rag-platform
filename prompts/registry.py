from prompts.base_prompt import BasePrompt

# Import prompt frameworks so they register themselves
import prompts.craft
import prompts.crispe


def get_prompt_framework(name: str):
    """
    Returns an instance of the selected prompt framework.
    """

    if name not in BasePrompt.registry:
        raise ValueError(f"Prompt framework '{name}' not supported")

    return BasePrompt.registry[name]()


def list_prompt_frameworks():
    """
    Returns all available prompt frameworks.
    Useful for populating UI dropdowns.
    """

    return list(BasePrompt.registry.keys())