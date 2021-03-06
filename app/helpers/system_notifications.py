"""
User Notification Structures
"""
from app.models.notifications import (
    EVENT_ROLE_INVITE,
    NEW_SESSION,
    SESSION_SCHEDULE,
    NEXT_EVENT,
    SESSION_ACCEPT_REJECT,
    INVITE_PAPERS,
    AFTER_EVENT,
    EVENT_PUBLISH,
    USER_CHANGE_EMAIL,
    TICKET_PURCHASED,
    EVENT_EXPORT_FAIL,
    EVENT_EXPORTED,
)

NOTIFS = {
    EVENT_EXPORTED: {
        'recipient': 'User',
        'title': 'Event {event_name} has been exported',
        'message': (
            "Event <strong>{event_name}</strong> has been exported successfully."
            "<br><br><a href='{download_url}' class='btn btn-info btn-sm'>Download</a>"
        )
    },
    EVENT_EXPORT_FAIL: {
        'recipient': 'User',
        'title': 'Export of event {event_name} failed',
        'message': (
            "The following error occured:<br>"
            "<pre>{error_text}</pre>"
        )
    },
    TICKET_PURCHASED: {
        'recipient': 'User',
        'title': 'Your order invoice and tickets ({invoice_id})',
        'message': (
            "Your order has been processed successfully."
            "<br><br><a href='{order_url}' class='btn btn-info btn-sm'>View Invoice</a>"
        )
    },
    USER_CHANGE_EMAIL: {
        'recipient': 'User',
        'title': 'Your email has been changed',
        'message': (
            "Your email has been changed from {email} to {new_email}.<br>Please verify your new email."
        )
    },
    AFTER_EVENT: {
        'title': 'Event {event_name} completed',
        'message': """The event <strong>{event_name}</strong> has been completed.<br><br>""",
        'recipient': 'User',
    },
    EVENT_PUBLISH: {
        'title': 'Event {event_name} has been published',
        'message': """The event <strong>{event_name}</strong> has been published.<br><br>
                   <a href='{link}' class='btn btn-info btn-sm'>View Event</a>""",
        'recipient': 'User',
    },
    EVENT_ROLE_INVITE: {
        'title': 'Invitation to be {role_name} at {event_name}',
        'message': """You've been invited to be a <strong>{role_name}</strong>
            at <strong>{event_name}</strong>.<br><br>
            <a href='{accept_link}' class='btn btn-success btn-sm'>Accept</a>
            <a href='{decline_link}' class='btn btn-danger btn-sm'>Decline</a>""",
        'recipient': 'User',
    },
    NEW_SESSION: {
        'title': 'New session proposal for {event_name}',
        'message': """The event <strong>{event_name}</strong> has received
             a new session proposal.<br><br>
            <a href='{link}' class='btn btn-info btn-sm'>View Session</a>""",
        'recipient': 'Organizer',
    },
    SESSION_SCHEDULE: {
        'title': 'Schedule for Session {session_name} has been changed',
        'message': """The schedule for session <strong>{session_name}</strong>
             has been changed.<br><br>
            <a href='{link}' class='btn btn-info btn-sm'>View Session</a>""",
        'recipient': 'Organizer, Speaker',
    },
    NEXT_EVENT: {
        'title': 'Event {event_name} is coming soon',
        'message': """Here are upcoming events: {up_coming_events}.<br><br>
            <a href='{link}' class='btn btn-info btn-sm'>View Event</a>""",
        'recipient': 'Organizer, Speaker',
    },
    SESSION_ACCEPT_REJECT: {
        'title': 'Session {session_name} has been {acceptance}',
        'message': """The session <strong>{session_name}</strong> has been
             <strong>{acceptance}</strong> by the Organizer.<br><br>
            <a href='{link}' class='btn btn-info btn-sm'>View Session</a>""",
        'recipient': 'Speaker',
    },
    INVITE_PAPERS: {
        'title': 'Invitation to Submit Papers for {event_name}',
        'message': """You have been invited to submit papers for <strong>{event_name}</strong>.<br><br>
            <a href='{cfs_link}' class='btn btn-info btn-sm'>View Call for Speakers</a>
            <a href='{submit_link}' class='btn btn-success btn-sm'>Submit</a>""",
        'recipient': 'Speaker',
    },
}
