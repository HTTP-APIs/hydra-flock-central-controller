echo "Install requirements..."
pip install -r requirements.txt
echo "Removing Hydrus if exists.."
rm -rf hydrus

git clone -b develop git@github.com:HTTP-APIs/hydrus.git hydrus

echo "Copying APIDocumentation to hydrus.."
cp flock_controller/api_docs/doc_gen.py hydrus/hydrus/metadata/
echo "Updating hydrus settings.."
cp flock_controller/settings.py hydrus/hydrus/

echo "Initializing Drone database.."
python flock_controller/db_init.py

python hydrus/hydrus/app.py
