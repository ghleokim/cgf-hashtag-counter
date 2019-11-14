## checklist 

- [ ] make log writer work well(separate it)
- [ ] support raspberrypi/macOS envs
- [ ] deal with unicode Errors


## folder structure

```
root/
    readme.md
    run.py
    counter.py
    source/
        
```


## log

```
root/
    log/
        index/
            log.txt
            timeindex.json
        count/
            {keyword}.txt
        search_history/
            {keyword}/
                {timestamp}_BIG.json
                {timestamp}_SHORT.json
```

logging의 경우 용도별로 파일과 폴더를 분리해 두었다.

- `index/`: 파일 실행, 오류 등 전반적인 내용을 기록하는 `log.txt`, keyword와 실행 시간을 기준으로 파일명을 찾을 수 있도록 하는 `timeindex.json`를 만들었다.
- `count/`: script가 사용하는 데이터, count의 변화를 기록한다.
- `search_history/`: keyword별로 디렉토리를 만들어 크롤링한 데이터를 json 파일로 저장한다.