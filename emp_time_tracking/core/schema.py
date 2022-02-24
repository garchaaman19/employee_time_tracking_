# from curses.ascii import US
from sqlite3 import Time
import graphene
from graphene_django import DjangoObjectType
from .models import User,TimeEntry
import json
import graphql_jwt
#schema describes our data models which we give to graphql server 

class UsersType(DjangoObjectType):
    class Meta:
        model = User
        fields=("id","username","email")

class ClockedHoursType(DjangoObjectType):
    class Meta:
        model= TimeEntry
        fields=("clock_in","clock_out")


class Query(graphene.ObjectType):
    all_users=graphene.List(UsersType)
    hello=graphene.String()
    today= graphene.List(ClockedHoursType)
    currentWeek= graphene.String()
    currentMonth= graphene.String()

    def resolve_all_users(root,info): # root is entry point, info allows to pass some info
        return User.objects.all()

    def resolve_today(root,info):
        pass

    def resolve_monthly(root,info):
        pass

    def resolve_weekly(root,info):
        pass

class CreateUserMutation(graphene.Mutation):
    class Arguments:
        email=graphene.String()
        username=graphene.String()
        password=graphene.String()
    
    user=graphene.Field(UsersType)

    @classmethod
    def mutate(cls,root,info,email,username,password):
        user=User(email=email,username=username,password=password)
        user.save()
        return CreateUserMutation(user=user)

class AuthMutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()



class Mutation(AuthMutation,graphene.ObjectType):
    createUser=CreateUserMutation.Field()

schema=graphene.Schema(query=Query,mutation=Mutation)
