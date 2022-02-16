from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as Dwait
from selenium.webdriver.support.expected_conditions import presence_of_element_located as isPresent
from keyboard import is_pressed, wait
from easygui import enterbox
from easygui import fileopenbox

xp_of_plus_btn = "/html/body/div[1]/header/div[6]/details/summary"
xp_for_license = r"/html/body/div[6]/main/div/form/div[6]/div[4]/div[3]/span[2]/details/summary/span[2]"
mit_xp = r"/html/body/div[6]/main/div/form/div[6]/div[4]/div[3]/span[2]/details/details-menu/div/div/div/label[4]/div/div[1]"
create_repository_xp = r"/html/body/div[6]/main/div/form/div[6]/button"
add_file = r"/html/body/div[6]/div/main/div[2]/div/div/div[3]/div[1]/div[2]/details/summary"
upload = "/html/body/div[6]/div/main/div[2]/div/div/div[3]/div[1]/div[2]/details/div/ul/li[4]/a"
commit_changes = r"/html/body/div[6]/div/main/div[2]/div/form/button"


driver = Chrome(CM().install())
driver.get(r"https://github.com/login")

def byid(id):
    return driver.find_element(By.ID,id)

def byxp(xp):
    return driver.find_element(By.XPATH,xp)

def bylt(txt):
    return driver.find_element(By.LINK_TEXT,txt)

print("Login To GitHub")
Dwait(driver,300).until(isPresent((By.XPATH,xp_of_plus_btn)))

while not is_pressed("esc"):
    
    byxp(xp_of_plus_btn).click()
    bylt("New repository").click()
    
    upload_files = fileopenbox(msg="Upload files", title="Github", multiple=True)
    repo_name = upload_files[0].split("\\")[-1]
    
    if repo_name is None:
        print("Fatal Error:Invalid Repository Name.........")
        exit(0)
    print("Upload Files:\n\n")
    for i in upload_files:
        print(i)
    
    byid("repository_name").send_keys(repo_name)  
    byid("repository_auto_init").click()
    byid("repository_license_template_toggle").click()
    
    byxp(xp_for_license).click()
    byxp(mit_xp).click()
    
    byxp(create_repository_xp).click()
    
    Dwait(driver,200).until(isPresent((By.XPATH,add_file)))
    
    byxp(add_file).click()
    byxp(upload).click()
    
    upload_element = byid("upload-manifest-files-input")

    for i in upload_files:
        print(i)
        upload_element.send_keys(i)
        
    byxp(commit_changes).click()
    wait("alt")
    driver.get("https://github.com/yrzgithub")