"""Step 5: Wrap the retriever as  a tool the agent can call."""

from langchain.tools import tool

def create_search_tool(retriever):
    """
    Return a @tool fuction that searches the HR policy document.
    """
    @tool
    def search_hr_policy(question: str) -> str:
        """Search the HR Policy document for information about leave, work from home,
        probation, notice period, reimbursement, code of conduct, holidays, or exit process."""
        matchin_chunks= retriever.invoke(question)
        return '\n\n'.join(chunk.page_content for chunk in matchin_chunks)

    return search_hr_policy


