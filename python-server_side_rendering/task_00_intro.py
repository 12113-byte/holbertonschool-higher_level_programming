def generate_invitations(template, attendees):
    if type(template) is str and type(attendees) is list:
        if not template:
            print('Template is empty, no output files generated.')
            return
        elif not attendees:
            print('No data provided, no output files generated.')
            return 
    else:
        print('Wrong format')
        return
    for attendee in attendees:
        content = template.replace('{name}', attendee.get('name') or 'N/A')
        content = content.replace('{event_title}', attendee.get('event_title') or 'N/A')
        content = content.replace('{event_date}', attendee.get('event_date') or 'N/A')
        content = content.replace('{event_location}', attendee.get('event_location') or 'N/A')
