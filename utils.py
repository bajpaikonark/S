import os

def retrieve_answer(query: str) -> str:
    # Very simple mock retrieval for demo
    if "plant" in query.lower():
        return "Plants make their own food using photosynthesis."
    elif "animal" in query.lower():
        return "Animals depend on plants and other animals for food."
    else:
        return "I’m not sure, try asking in a different way!"
