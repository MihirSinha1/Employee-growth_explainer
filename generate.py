from image import load_employee_graphs
import base64
import os
from openai import OpenAI
from io import BytesIO

from openai import OpenAI
import base64
from io import BytesIO

def generate_graph_insights_openai(api_key, employee_name: str, images: dict):
    client = OpenAI(api_key=api_key)
    

    # Convert all images to base64 and prepare content blocks
    content_blocks = [
        {"type": "text", "text": f"Compare these 4 graphs for employee's compensation {employee_name} and generate insights that might be useful for manager to understand the compenstion better in 1-2 sentences and mention some helpful suggetions if required also 1-2 sentenses."}
    ]

    for filename, img in images.items():
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

        content_blocks.append({
            "type": "image_url",
            "image_url": {"url": f"data:image/png;base64,{img_base64}"}
        })
        # Correct format: messages[0]["content"] is a list of dicts
    response = client.chat.completions.create(
    model="gpt-4o-mini",  # or "gpt-4o"
    messages=[{"role": "user", "content": content_blocks}],
    max_tokens=800
    )


        # Extract text response
    insight = response.choices[0].message.content if response.choices else "No insight generated."
    

    return insight

# import base64
# from io import BytesIO
# from openai import OpenAI

# def generate_employee_summary(api_key: str, employee_name: str, images: dict):
#     """
#     Use OpenAI GPT-4o to compare multiple graphs and generate a summary.

#     Args:
#         api_key (str): Your OpenAI API key.
#         employee_name (str): Name of the employee.
#         images (dict): Dictionary of {filename: PIL.Image}.

#     Returns:
#         str: Insight summary across all graphs.
#     """
#     client = OpenAI(api_key=api_key)

#     # Convert all images to base64 and prepare content blocks
#     content_blocks = [
#         {"type": "text", "text": f"Compare these 4 graphs for employee {employee_name} and generate insights."}
#     ]

#     for filename, img in images.items():
#         buffer = BytesIO()
#         img.save(buffer, format="PNG")
#         img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

#         content_blocks.append({
#             "type": "image_url",
#             "image_url": {"url": f"data:image/png;base64,{img_base64}"}
#         })

#     # Send all graphs in one request
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",  # or "gpt-4o"
#         messages=[{"role": "user", "content": content_blocks}],
#         max_tokens=800
#     )

#     return response.choices[0].message.content



# base_folder = "Employee Graphs"  # root folder containing employee subfolders
# employee = "Employee 1"

# graphs = load_employee_graphs(base_folder, employee)
# insights=generate_graph_insights_openai(employee,graphs)
# print(insights)







#import base64
# import os
# from anthropic import Anthropic
# from image import load_employee_graphs
# from openai import OpenAI
# def generate_graph_insights( employee_name: str, images: dict):
#     """
#     Use Claude 3.5 Sonnet to generate insights for each graph image.

#     Args:
#         api_key (str): Your Anthropic API key.
#         employee_name (str): Name of the employee.
#         images (dict): Dictionary of {filename: PIL.Image} from load_employee_graphs().

#     Returns:
#         dict: {filename: insight_text}
#     """
#     client = Anthropic(api_key="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")
#     insights = {}

#     for filename, img in images.items():
#         # Convert image to base64
#         img_bytes = img.tobytes()
#         buffered = img.convert("RGB")
#         from io import BytesIO
#         buffer = BytesIO()
#         buffered.save(buffer, format="PNG")
#         img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

#         # Send to Claude
#         response = client.messages.create(
#             model="claude-3-5-sonnet",
#             max_tokens=500,
#             messages=[
#                 {
#                     "role": "You are an employees increment explainer on the basis of data like their increment comparision to their peer,makrket etc.",
#                     "content": [
#                         {"type": "text", "text": f"Explain the increment trends in this graph for employee {employee_name}."},
#                         {"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": img_base64}}
#                     ]
#                 }
#             ]
#         )

#         # Extract text response
#         insight = response.content[0].text if response.content else "No insight generated."
#         insights[filename] = insight

#     return insights