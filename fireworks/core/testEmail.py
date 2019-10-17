import smtplib


class Emailer:

    launchId: object

    def __init__(self, content, launchid, state):
        from_addr = 'gleam.x.workflow@gmail.com'
        to_addr = 'kramer.ian.thomas@gmail.com'
        subject = "TASK: " + str(launchid) + " " + str(state)
        content = ("Work flow \n\t Task ID: " + str(launchid) + " \nFinished with State: " + str(state))


        body = "\r\n".join((
            "From: %s" % from_addr,
            "To: %s" % to_addr,
            "Subject: <%s>" % subject,
            "",
            content
        ))
        mail = smtplib.SMTP('smtp.gmail.com', 587)

        # indify yourself to server
        # helo for reqular
        # ehlo for esmtp
        mail.ehlo()

        # start tls mode
        # Transport layer security
        # Any smtp command after this will be encrrypted. Want our login process encrypted

        mail.starttls()

        mail.login('gleam.x.workflow@gmail.com', 'CIRAX2020')

        mail.sendmail('gleam.x.workflow@gmail.com', 'kramer.ian.thomas@gmail.com', body)

        mail.close()
