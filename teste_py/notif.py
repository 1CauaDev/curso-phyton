from winotify import Notification,audio

notificacao = Notification(app_id ="lembrete",title ="notificacao da Agenda",
                           msg="Lembrete, sua prova sera dia --/--/---",
                           duration="short", icon=r"C:\Users\Cauã\Downloads\agenda.png")
notificacao.set_audio(audio.Mail, loop=False)
notificacao.add_actions(label="Acesse nossa Agenda", launch="https://calendario2018brasil.com.br/")
notificacao.show()