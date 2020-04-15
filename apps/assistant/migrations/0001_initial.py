# Generated by Django 3.0.5 on 2020-04-15 21:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatsonComponents',
            fields=[
                ('pk_watson_components', models.CharField(choices=[('Watson Studio', 'Aprendizado de Máquina Embarcado'), ('Watson Machine Learning', 'Aprendizado de Máquina'), ('Compare and Comply', 'Processamento de Documentos'), ('Discovery', 'Busca Analítica de Conteúdo'), ('Knowledge Catalog', 'Busca, Cataloga e Compartilha Documentos'), ('Knowledge Studio', 'Aprendizado de Linguagem de Domínio'), ('Language Translator', 'Tradutor de Linguagens'), ('Natural Language Understanding', 'Analisador de Textos'), ('Personality Insights', 'Gerar Perfil Psicológico'), ('SpeechToText', 'Reconheciento de Fala'), ('TextToSpeech', 'Transforma Texto em Fala'), ('Visual Recognition', 'Reconhecimento de Imagens')], max_length=50, primary_key=True, serialize=False, verbose_name='Tipo Componente')),
                ('dsc_comp', models.CharField(max_length=100, verbose_name='Descrição')),
                ('insert_date', models.DateTimeField(auto_now_add=True, verbose_name='Data Inserção')),
                ('update_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Data Edição')),
            ],
            options={
                'verbose_name': 'Componentes IBM Watson',
                'verbose_name_plural': 'Componentes IBM Watson',
                'db_table': 'watson_components',
            },
        ),
        migrations.CreateModel(
            name='WatsonLogs',
            fields=[
                ('pk_watson_logs', models.AutoField(primary_key=True, serialize=False, verbose_name='Código')),
                ('sender_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome do Usuário')),
                ('sender_message', models.TextField(verbose_name='Mensagem Enviada')),
                ('response_message', models.TextField(verbose_name='Resposta da Mensagem')),
                ('flag_invalid_response', models.SmallIntegerField(choices=[(0, 'Não'), (1, 'Sim')], default=0, verbose_name='Resposta Inválida')),
                ('flag_resolve', models.SmallIntegerField(choices=[(0, 'Não'), (1, 'Sim')], default=0, verbose_name='Resolvida')),
                ('insert_date', models.DateTimeField(auto_now_add=True, verbose_name='Data Inserção')),
                ('update_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Data Edição')),
                ('fk_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
                ('fk_watson_components', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assistant.WatsonComponents', verbose_name='Componente')),
            ],
            options={
                'verbose_name': 'Log de Mensagens',
                'verbose_name_plural': 'Log de Mensagens',
                'db_table': 'watson_logs',
            },
        ),
        migrations.CreateModel(
            name='WatsonAccess',
            fields=[
                ('pk_watson_access', models.AutoField(primary_key=True, serialize=False, verbose_name='Código')),
                ('component_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome do Componente')),
                ('component_key', models.CharField(default='', max_length=180, verbose_name='API Key')),
                ('component_url', models.TextField(default='https://', verbose_name='URL')),
                ('insert_date', models.DateTimeField(auto_now_add=True, verbose_name='Data Inserção')),
                ('update_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Data Edição')),
                ('fk_assistants', models.ManyToManyField(to='core.Assistants')),
                ('fk_watson_components', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assistant.WatsonComponents', verbose_name='Componente')),
            ],
            options={
                'verbose_name': 'Chaves Accesso Componentes',
                'verbose_name_plural': 'Chaves Accesso Componentes',
                'db_table': 'watson_access',
            },
        ),
        migrations.AddIndex(
            model_name='watsonlogs',
            index=models.Index(fields=['fk_user', 'fk_watson_components', 'flag_invalid_response'], name='watson_logs_fk_user_e3f9b3_idx'),
        ),
    ]
