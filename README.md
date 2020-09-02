## **File Processor**

This service allows to load UserSchema JSON files to S3. It's the first stage in the data ingestion process.

### Getting Ready

```python
from src.profile_processor.Facade.ProfileProcessor import ProfileProcessor
ProfileProcessor.save(USERDATASCHEMA)
```

Where USERDATASCHEMA represent the UserSchema we want to load into the S3 Bucket.

### Test

To run the whole suite run
```
pytest
```
