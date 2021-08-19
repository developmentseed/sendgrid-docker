Simple Docker container that reads environment variables and sends a single email using the SendGrid API.

We needed this to send out job failure notifications on a k8s cluster, and did not find an existing Docker image to do this, so created this as a simple standalone project / docker image that could be used in different contexts.

Required environment variables:

 - SENDGRID_API_KEY
 - FROM_EMAIL
 - TO_EMAILS
 - EMAIL_SUBJECT
 - EMAIL_MESSAGE



