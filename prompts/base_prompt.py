class BasePrompt:

    registry = {}

    def __init_subclass__(cls, framework_name=None, **kwargs):
        super().__init_subclass__(**kwargs)

        if framework_name:
            BasePrompt.registry[framework_name] = cls

    def build_prompt(self, query, context):
        raise NotImplementedError