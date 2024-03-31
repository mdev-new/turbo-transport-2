# class User(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     username = models.CharField(max_length=30)
#     pass_hash = models.TextField()
#
#
# class Station(models.Model):
#     pass
#
#
# class Search(models.Model):
#     # Delete the entry when either user, source or destination get removed
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     source = models.ForeignKey(Station, on_delete=models.CASCADE)
#     destination = models.ForeignKey(Station, on_delete=models.CASCADE)
#     urge = models.IntegerField()  # Todo maybe IntegerChoiceField
#     walk_speed = models.FloatField()
