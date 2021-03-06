# -*- coding: utf-8 -*-
"""Upto_Midsem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ljDOYMg1_4E4vCZPkOK3TAivh38K1QET
"""

#code to convert audio files .wav to genre_dic={'jazz':[list of numpy array of 3 sec audio],..}
#Breaking every audio into 10 clips
n=10
genres = 'blues classical country disco hiphop jazz metal pop reggae rock'.split()
genre_dic={}
for g in genres:
  genre_dic[g]=[]
for g in genres:
  print(g)
  audio_path2='/content/drive/My Drive/ML_project_Data/genres_original/'+g+'/'
  for i in range(10):
    #print(g+str(i))
    audio_path3=audio_path2+g+'.0000'+str(i)+'.wav'
    x, sr = librosa.load(audio_path3, sr=22050)
    k=0
    inc=x.shape[0]//n
    for j in range(n):
      x_new=x[k:k+inc]
      k+=inc
      genre_dic[g].append(x_new)
  
  for i in range(10,100):
    #print(g+str(i))
    audio_path3=audio_path2+g+'.000'+str(i)+'.wav'
    x, sr = librosa.load(audio_path3, sr=22050)
    k=0
    inc=x.shape[0]//n
    for j in range(n):
      x_new=x[k:k+inc]
      k+=inc
      genre_dic[g].append(x_new)
print('completed')

#saving genre_dic to external file
np.savez('/content/drive/My Drive/ML_project_Data/data2.npz',**genre_dic)

#reading audio data from npz file
genre_dic2=np.load('/content/drive/My Drive/ML_project_Data/data2.npz')

#Saving Spectrogram for every Audio
import matplotlib.pyplot as plt
import pathlib
cmap=plt.get_cmap('inferno')
plt.figure(figsize=(10,10))
genres = 'blues classical country disco hiphop jazz metal pop reggae rock'.split()

for g in genres:
  k=0
  pathlib.Path(f'/content/drive/My Drive/ML_project_Data/Spectrogram/{g}').mkdir(parents=True, exist_ok=True)
  for i in range(10):
    for j in range(10):
      short_new_clip=genre_dic[g][k]
      plt.specgram(short_new_clip, NFFT=2048, Fs=2, Fc=0, noverlap=128, cmap=cmap, sides='default', mode='default', scale='dB');
      plt.axis('off');
      plt.savefig(f'/content/drive/My Drive/ML_project_Data/Spectrogram/{g}/{g}' + '.0000'+str(i)+'.'+str(j)+'.png')
      plt.clf()
      k+=1
  for i in range(10,100):
    for j in range(10):
      gshort_new_clip=genre_dic[g][k]
      plt.specgram(short_new_clip, NFFT=2048, Fs=2, Fc=0, noverlap=128, cmap=cmap, sides='default', mode='default', scale='dB');
      plt.axis('off');
      plt.savefig(f'/content/drive/My Drive/ML_project_Data/Spectrogram/{g}/{g}'+'.000'+str(i)+'.'+str(j)+'.png')
      plt.clf()
      k+=1



#code to convert audio data to feature csv file
import librosa
import numpy as np
import csv
sr=22050
header_temp = 'chroma_stft rmse spectral_centroid spectral_bandwidth rolloff zero_crossing_rate'.split()
header = 'filename'
for h in header_temp:
  header+=' '+h+'_mean'
  header+=' '+h+'_var'
for i in range(1,21):
  header+=' mfcc'+str(i)+'_mean'
  header+=' mfcc'+str(i)+'_var'
header+=' label'
header=header.split()
file=open('/content/drive/My Drive/ML_project_Data/our_features_3_sec.csv','w',newline='')
with file:
  writer=csv.writer(file)
  writer.writerow(header)
genres = 'blues classical country disco hiphop jazz metal pop reggae rock'.split()
for g in genres:
  print(g)
  k=0
  for i in range(10):
    for j in range(10):
      short_new_clip=genre_dic[g][k]
      mfcc=librosa.feature.mfcc(y=short_new_clip,sr=sr)
      chroma_stft=librosa.feature.chroma_stft(y=short_new_clip,sr=sr)
      spectral_centroid=librosa.feature.spectral_centroid(y=short_new_clip,sr=sr)
      zero_crossing_rate=librosa.feature.zero_crossing_rate(short_new_clip)
      spectral_bandwidth=librosa.feature.spectral_bandwidth(y=short_new_clip,sr=sr)
      rms=librosa.feature.rmse(y=short_new_clip)
      rolloff=librosa.feature.spectral_rolloff(y=short_new_clip,sr=sr)
      filename=g + '.0000'+str(i)+'.'+str(j)+'.wav'
      row=f'{filename} {np.mean(chroma_stft)} {np.var(chroma_stft)} {np.mean(rms)} {np.var(rms)} {np.mean(spectral_centroid)} {np.var(spectral_centroid)} {np.mean(spectral_bandwidth)} {np.var(spectral_bandwidth)} {np.mean(rolloff)} {np.var(rolloff)} {np.mean(zero_crossing_rate)} {np.var(zero_crossing_rate)}'
      for mfc in mfcc:
        row+=f' {np.mean(mfc)} {np.var(mfc)}'
      row+=f' {g}'
      file=open('/content/drive/My Drive/ML_project_Data/our_features_3_sec.csv','a',newline='')
      with file:
        writer=csv.writer(file)
        writer.writerow(row.split())
      k+=1
  for i in range(10,100):
    for j in range(10):
      short_new_clip=genre_dic[g][k]
      mfcc=librosa.feature.mfcc(y=short_new_clip,sr=sr)
      chroma_stft=librosa.feature.chroma_stft(y=short_new_clip,sr=sr)
      spectral_centroid=librosa.feature.spectral_centroid(y=short_new_clip,sr=sr)
      zero_crossing_rate=librosa.feature.zero_crossing_rate(short_new_clip)
      spectral_bandwidth=librosa.feature.spectral_bandwidth(y=short_new_clip,sr=sr)
      rms=librosa.feature.rmse(y=short_new_clip)
      rolloff=librosa.feature.spectral_rolloff(y=short_new_clip,sr=sr)
      filename=g + '.000'+str(i)+'.'+str(j)+'.wav'
      row=f'{filename} {np.mean(chroma_stft)} {np.var(chroma_stft)} {np.mean(rms)} {np.var(rms)} {np.mean(spectral_centroid)} {np.var(spectral_centroid)} {np.mean(spectral_bandwidth)} {np.var(spectral_bandwidth)} {np.mean(rolloff)} {np.var(rolloff)} {np.mean(zero_crossing_rate)} {np.var(zero_crossing_rate)}'
      for mfc in mfcc:
        row+=f' {np.mean(mfc)} {np.var(mfc)}'
      row+=f' {g}'
      file=open('/content/drive/My Drive/ML_project_Data/our_features_3_sec.csv','a',newline='')
      with file:
        writer=csv.writer(file)
        writer.writerow(row.split())
      k+=1
print('completed')



#saving new 3 sec audio clips
import matplotlib.pyplot as plt
import pathlib
import time
import librosa.display
sr=22050
#plt.figure(figsize=(10,10))
genres = 'blues classical country disco hiphop jazz metal pop reggae rock'.split()
for g in genres:
  print(g)
  k=0
  pathlib.Path(f'/content/drive/My Drive/ML_project_Data/New_Audio/{g}').mkdir(parents=True, exist_ok=True)
  for i in range(10):
    for j in range(10):
      short_new_clip=genre_dic[g][k]
      librosa.output.write_wav(f'/content/drive/My Drive/ML_project_Data/New_Audio/{g}/'+ g  + '.0000'+str(i)+'.'+str(j)+'.wav', short_new_clip, sr)
      k+=1
      time.sleep(0.1)
  for i in range(10,100):
    for j in range(10):
      short_new_clip=genre_dic[g][k]
      librosa.output.write_wav(f'/content/drive/My Drive/ML_project_Data/New_Audio/{g}/'+ g + '.000'+str(i)+'.'+str(j)+'.wav', short_new_clip, sr)
      k+=1
      time.sleep(0.1)
print('completed')


#saving plots of new 3 sec audio clips
import matplotlib.pyplot as plt
import pathlib
import librosa.display
sr=22050
genres = 'blues classical country disco hiphop jazz metal pop reggae rock'.split()
for g in genres:
  print(g)
  k=0
  pathlib.Path(f'/content/drive/My Drive/ML_project_Data/New_Audio_plots/{g}').mkdir(parents=True, exist_ok=True)
  for i in range(10):
    for j in range(10):
      short_new_clip=genre_dic[g][k]
      plt.title('Audio File'+ g  + '.0000'+str(i)+'.'+str(j)+'.wav')
      plt.xlabel('Time')
      librosa.display.waveplot(short_new_clip, sr)
      plt.savefig(f'/content/drive/My Drive/ML_project_Data/New_Audio_plots/{g}/'+ g  + '.0000'+str(i)+'.'+str(j)+'.png')
      plt.clf()
      k+=1
  for i in range(10,100):
    for j in range(10):
      short_new_clip=genre_dic[g][k]
      plt.title('Audio File'+ g  + '.000'+str(i)+'.'+str(j)+'.wav')
      plt.xlabel('Time')
      librosa.display.waveplot(short_new_clip, sr)
      plt.savefig(f'/content/drive/My Drive/ML_project_Data/New_Audio_plots/{g}/'+ g  + '.000'+str(i)+'.'+str(j)+'.png')
      plt.clf()
      k+=1
print('completed')