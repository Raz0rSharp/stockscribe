from .models import Subscription

def cron_job():
    #dictionary of email to object
    #for each email: for each object, add to string ticker and price
    #send the email

    subscriptions = Subscription.objects.all()
    sub_emails = {}
    for sub in subscriptions:
        if (sub.email not in sub_emails):
            sub_emails[sub.email] = [sub]
        else:
            sub_emails[sub.email].append(sub)
    for x in sub_emails:
        email_subs = grouped[x]
        sub_list = ""
        for item in email_subs:
            sub_list += item.ticker + " $" + "{:,}".format(round(si.get_live_price(item.ticker), 2)) + "\n"
        send_mail(
        'Your Stock Subscriptions',
        sub_list,
        'nick.lesho@gmail.com',
        [x],
        fail_silently=False,
        )
