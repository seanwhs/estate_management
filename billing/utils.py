from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

from django.core.mail import EmailMessage
from django.conf import settings

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def email_bill(to_email, from_client, filepath):
    from_email = settings.EMAIL_HOST_USER
    subject = '[Sean\'s] Bill Test'
    body = """
    Good day,

    Please find attached bill from {} for your immediate attention.

    regards,
    Sean's Lab
    """

    message = EmailMessage(subject, body, from_email, [to_email])
    message.attach_file(filepath)
    message.send()
