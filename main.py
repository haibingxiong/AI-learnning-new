from prompt_template import system_template_text, user_template_text
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from text_type import text_type
def xiaohongshu_generate(subject,openai_key):
    ###prompt
    prompt= ChatPromptTemplate.from_messages(
        [("system", system_template_text),
         ("user", user_template_text)])
    ###model
    model=ChatOpenAI(model='gpt-4',
                     api_key=openai_key
                     )
    ###output_parser
    output_parser= PydanticOutputParser(pydantic_object=text_type)

    chain= prompt | model | output_parser

    output= chain.invoke(
        {"subject": subject,
        "parser_instructions": output_parser.get_format_instructions()}
    )
    return output