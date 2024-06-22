from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from src.external.cognito.cognito_remove_user import cognito_remove_user
from src.external.cognito.cognito_validate import CognitoValidate



class UsuarioDetalhesView(APIView):
    def delete(self, request, cpf: str):
        """
        Api para remover usuario
        """
        print('passou aqui')
        if request.META.get('HTTP_AUTHORIZATION'):
            if 'Bearer' in request.META.get('HTTP_AUTHORIZATION'):
                header = request.META.get('HTTP_AUTHORIZATION')
                token = header.split(" ")[1]
                try:
                    token_validado = CognitoValidate.validar_token(token)
                    if cpf == token_validado['Username']:
                        cognito_remove_user(cpf)
                        return Response(status=status.HTTP_204_NO_CONTENT)
                    else:
                        return Response(data={'token informado invalido'}, status=status.HTTP_400_BAD_REQUEST)
                except Exception as e:
                    print(e)
                    return Response(data={'token informado invalido'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'erro' : 'Necessario realizar login para executar essa acao.'}, status=status.HTTP_403_FORBIDDEN)

