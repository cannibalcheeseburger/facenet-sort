
# environment-setup

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

Tool to sort photos by faces

ps: it works (for now)

## Installation

### Build from Source

Clone the repository and checkout to stable commit

```
git clone https://github.com/cannibalcheeseburger/facenet-sort.git
cd facenet-sort
```

### Install Requirements

For pipenv:
```
pipenv install
```
For pip:
```
pip install -r requirements.txt
```

## Usage

1. Create basic folder structure using (also used to populate `INPUT` and `OUTPUT` folders)

    ```
    python clean.py
    ```

2. Populate `data/train/` folder with folders containing images of people and folder names corresponding to person name

    Eg. `data/train/kash/`

    Then run the `prepare.py` script:
    
    ```
    python prepare.py
    ```  

3. Feed images of people you want to sort in `INPUT` folder and run `run.py` script

    ```
    python run.py
    ```

### Contact / Social Media

<a href = "https://www.github.com/cannibalcheeseburger/">
    <img src = "https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/github.svg"  width="30" height="30">
</a>
 
<a href = "https://www.twitter.com/cannibalcheese/">
    <img src = "https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/twitter.svg"  width="30" height="30">
</a>

<a href = "https://www.instagram.com/cannibalcheeseburger/">
    <img src = "https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/instagram.svg"  width="30" height="30">
</a>

<a href = "https://www.facebook.com/kashish.srivastava.351/">
    <img src = "https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/facebook.svg"  width="30" height="30">
</a>

Email: kashish.srivastava014@gmail.com
### Developed by

Developer / Author: [Kashish Srivastava](https://github.com/cannibalcheeseburger/)


