# python-docker

#### 1. Create a directory with a name "python-docker"
`
mkdir python-docker
`
#### 2. Navigate to the newly created directory
`
cd python-docker
`
#### 3. Create a virtual environment
##### Windows
`
py -3 -m venv venv
`

#### macOS/Linux

`
python3 -m venv venv
`

#### 4. Activate the environment
##### Windows

`
venv\Scripts\activate
`
##### macOS/Linux

`
. venv/bin/activate or source venv/bin/activate
`
#### 5 .Install Flask
`
pip install Flask
`
#### 6. Run the `server1.py`
`
python server1.py
`
#### 7. Run the `server2.py`
`
python server2.py
`

#### 8. Run the `client.py` and input the city name, server 1 will return the zipcode based on the given city name from client. Server 2 will return the weather based on the given zipcode from client.
`
python client.py
`
###### Sample demo:
```
Enter a city name: Sunnyvale
<Response [200]>
zipcode: 94085
Weather for Sunnyvale: sunny
```
-----

### Some screenshots of the process:
![image](https://user-images.githubusercontent.com/112602900/216452918-f072b346-b60b-428f-b28f-16ac725ab7a6.png)

![image](https://user-images.githubusercontent.com/112602900/216452938-9d16d78a-9720-4fab-a823-4e8f0edf388a.png)
![image](https://user-images.githubusercontent.com/112602900/216452954-f9f6b591-3d4f-4328-84b3-c514f6fc60ee.png)
