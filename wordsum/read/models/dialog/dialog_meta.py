class Dialog_Meta(models.Model):
    dialog = models.BooleanField()
    dialog_being = models.BooleanField()
    dialog_continue = models.BooleanField()
    dialog_end  = models.BooleanField()


