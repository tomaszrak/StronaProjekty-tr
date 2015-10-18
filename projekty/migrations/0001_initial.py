# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projekt',
            fields=[
                ('id_projektu', models.CharField(max_length=30, serialize=False, verbose_name=b'ID projektu', primary_key=True)),
                ('nazwa', models.CharField(max_length=50, verbose_name=b'Nazwa projektu')),
                ('liczba_miejsc', models.IntegerField(max_length=100, verbose_name=b'Lb. miejsc')),
            ],
            options={
                'verbose_name_plural': 'Projekt',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Prowadzacy',
            fields=[
                ('id_prowadzacego', models.CharField(max_length=30, serialize=False, verbose_name=b'ID prowadzacego', primary_key=True)),
                ('nazwisko', models.CharField(max_length=30, verbose_name=b'Nazwisko')),
                ('imie', models.CharField(max_length=30, verbose_name=b'Imi\xc4\x99')),
                ('tytul', models.CharField(max_length=30, verbose_name=b'Tytu\xc5\x82')),
                ('stanowisko', models.CharField(max_length=30, verbose_name=b'Stanowisko')),
            ],
            options={
                'verbose_name_plural': 'Prowadz\u0105cy',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Przedmiot',
            fields=[
                ('id_przedmiotu', models.CharField(max_length=30, serialize=False, verbose_name=b'ID przedmiotu', primary_key=True)),
                ('nazwa', models.CharField(max_length=50, verbose_name=b'Nazwa przedmiotu')),
                ('tok_studiow', models.CharField(max_length=30, verbose_name=b'Tok studi\xc3\xb3w')),
                ('grupa', models.CharField(max_length=30, verbose_name=b'Grupa')),
                ('typ_zajec', models.CharField(max_length=50, verbose_name=b'Typ zaj\xc4\x99\xc4\x87')),
                ('id_prowadzacego', models.ForeignKey(to='projekty.Prowadzacy')),
            ],
            options={
                'verbose_name_plural': 'Przedmiot',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id_student', models.CharField(max_length=30, serialize=False, verbose_name=b'Numer indeksu', primary_key=True)),
                ('nazwisko', models.CharField(max_length=30, verbose_name=b'Nazwisko')),
                ('imie', models.CharField(max_length=30, verbose_name=b'Imi\xc4\x99')),
                ('tok_studiow', models.CharField(max_length=30, verbose_name=b'Tok studi\xc3\xb3w')),
            ],
            options={
                'verbose_name_plural': 'Student',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wybrany_projekt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('akceptacja', models.BooleanField(default=False, verbose_name=b'Akceptacja')),
                ('preferencja', models.CharField(max_length=30, verbose_name=b'Preferencja')),
                ('komentarz', models.CharField(max_length=100, verbose_name=b'Komentarz', blank=True)),
                ('licznosc_grupy', models.IntegerField(verbose_name=b'Liczno\xc5\x9b\xc4\x87 grupy')),
                ('id_projektu', models.ForeignKey(to='projekty.Projekt')),
                ('id_student', models.ForeignKey(to='projekty.Student')),
            ],
            options={
                'verbose_name_plural': 'Wybrany projekt',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='projekt',
            name='id_przedmiotu',
            field=models.ForeignKey(to='projekty.Przedmiot'),
            preserve_default=True,
        ),
    ]
