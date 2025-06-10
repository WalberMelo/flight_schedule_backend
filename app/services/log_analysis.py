
from app.core.config import settings
from app.models.schema import LogAnalysisRequest, LogAnalysisResponse
from openai import OpenAI

client = OpenAI(api_key=settings.OPENAI_API_KEY)

async def analyze_log(request: LogAnalysisRequest) -> LogAnalysisResponse:
    prompt = (
    "You are a certified aviation maintenance analyst specializing in general aviation (GA) aircraft. "
    "Read each maintenance log entry and provide:\n"
    "1. A clear, plain-language summary of the reported problem and action taken, using terminology familiar to maintenance teams.\n"
    "2. Identify if the failure is likely *acute* (sudden event) or *chronic* (wear/recurring issue), if possible.\n"
    "3. Flag any urgent safety or operational risks.\n"
    "4. List key affected systems, components, or fault codes mentioned (use aviation system language, e.g., 'hydraulics', 'oil pressure', 'flap mechanism').\n"
    "5. If you see a pattern or a possible recurring maintenance issue (such as electrical, sensor, or fluid leaks), mention it.\n"
    "\n"
    "Input format:\n"
    "IDENT: {ident}\n"
    "PROBLEM: {problem}\n"
    "ACTION: {action}\n"
    "\n"
    "Output format:\n"
    "Summary: <plain-language summary of the issue and fix>\n"
    "Failure Type: <Acute/Chronic/Unclear>\n"
    "Urgency: <Critical/Monitor/No Immediate Risk>\n"
    "Key Systems: <comma-separated list>\n"
    "Pattern: <Note if this is a common/recurring issue in GA maintenance, else 'None'>\n"
    "\n"
    "Example:\n"
    "Log:\n"
    "IDENT: 100002\n"
    "PROBLEM: ELECTRICAL SYSTEM FAULT DURING FLIGHT.\n"
    "ACTION: INSPECTED ALTERNATOR, FOUND LOOSE CONNECTION, RESECURED.\n"
    "Output:\n"
    "Summary: The pilot reported an in-flight electrical system issue. Maintenance found a loose alternator connection and resecured it.\n"
    "Failure Type: Acute\n"
    "Urgency: Monitor\n"
    "Key Systems: electrical system, alternator\n"
    "Pattern: Electrical system faults are a common cause of unplanned maintenance in GA aircraft, often related to connections or alternators.\n"
    "\n"
     f"Log:\n{request.log_text}\n"
    "IDENT: {ident}\n"
    "PROBLEM: {problem}\n"
    "ACTION: {action}\n"
    "Output:"
)

    completion = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.2)
    summary = completion.choices[0].message.content
    return LogAnalysisResponse(summary=summary)