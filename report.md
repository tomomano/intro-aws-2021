# レポート課題

## 課題1: EC2
自身の AWS Educate アカウントを用いて，以下の課題を実行せよ．

- [講義資料4章 (ハンズオン#1)](https://tomomano.github.io/learn-aws-by-coding/#sec_first_ec2) を自分の AWS Educate アカウントを使って実行し，EC2インスタンスを作成せよ．
その上で，以下の設問に答えよ．
- 作成したEC2仮想インスタンスにはランダムなIPv4アドレスが割り当てられる．
あなたが作成した EC2 インスタンスのアドレスを報告せよ．
- 作成したEC2インスタンスにログインし，次のコマンドを実行せよ．
コマンドの出力をレポートにコピー＆ペーストして報告せよ．
  - `$ cat /proc/cpuinfo`
  - `$ df -h`
- 作成したEC2インスタンスに[cowsay](https://en.wikipedia.org/wiki/Cowsay) と [fortune](https://en.wikipedia.org/wiki/Fortune_(Unix))をインストールせよ．
  - ヒント: `$ sudo yum install cowsay fortune-mod.x86_64`
- 次のコマンドを実行せよ．コマンドの出力をレポートにコピー＆ペースト (あるいはスクリーンショットでも良い) して報告せよ．
  - `$ fortune | cowsay`

## 課題2: Docker & ECS

まずは，自分のローカルのコンピュータで Docker を動かしてみよう．
- 自分のコンピュータに Docker をインストールせよ
- [講義資料8.3章](https://tomomano.github.io/learn-aws-by-coding/#_transformer_%E3%82%92%E7%94%A8%E3%81%84%E3%81%9F_question_answering_%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0) を参考に，本講義で提供している質問応答の Docker image (https://hub.docker.com/repository/docker/tomomano/qabot) を，**ローカルのコンピュータで**実行せよ．
- 自分で context と question の組み合わせを考え，プログラムがどのような答えを返したか，報告せよ．

つづいて，[講義資料8章](https://tomomano.github.io/learn-aws-by-coding/#sec_fargate_qabot) に書いてあるハンズオンを一通り自分自身の AWS Educate アカウントを用いて実行せよ．
- そのうえで，[講義資料8.7章](https://tomomano.github.io/learn-aws-by-coding/#_%E3%82%BF%E3%82%B9%E3%82%AF%E3%81%AE%E5%90%8C%E6%99%82%E5%AE%9F%E8%A1%8C) に従い，複数の質問を同時に投げかけた時の ECS クラスターのスケールの様子を確認せよ．
講義資料の Figure 49 に示したように， AWS Console から ECS のクラスターの挙動を確認し，スクリーンショットを撮り，レポートに報告せよ．
- そのほか，自由課題として，プログラムの一部を改変するなどして自由に実験を行ってみよ．
行った実験とその結果を報告せよ．

## 選択課題

選択課題は，2つのうちから1つを選択して解答する．

## 選択課題1: Serverless Arhictecture

- [Hellerstein et al., "Serverless Computing: One Step Forward, Two Steps Back
" arXiv (2018)](https://arxiv.org/abs/1812.03651) を読んで次の設問に答えよ．
- 著者らは，Serverless computing の利点と，MapReduceなど他の分散処理システムと比較した時の欠点や今後の課題を議論している．著者らの論点をまとめ，800文字以内で記述せよ．
- また，著者らの主張に対して，自分の意見や考えがある場合は，それも併せて記述せよ (その場合も，800文字以内の文字制限は変わらない)．

## 選択課題2: Serverless Application

[講義資料13章](https://tomomano.github.io/learn-aws-by-coding/#sec_bashoutter) を参考に， Serverless architecture (Lambda, DynamoDB, S3 など) を用いたオリジナルのウェブアプリケーションを構想し，実装せよ．
レポートでは，以下のものを提出すること．
- 実装する API のリストと，その機能を記述したテーブル
- スタックを構成するソースコード (AWS CDK や API のハンドラなど)
(レポートに直接コードを貼り付ける，クラウドストレージを通じて共有する，GitHub のリンクを送る，など教員が中身を確認できるようであれば提出の仕方は問わない)
- 実装した API の使用例とその実行結果 ([講義資料13.4章](https://tomomano.github.io/learn-aws-by-coding/#_api_%E3%83%AA%E3%82%AF%E3%82%A8%E3%82%B9%E3%83%88%E3%82%92%E9%80%81%E4%BF%A1%E3%81%99%E3%82%8B) を参考にせよ)

ウェブブラウザの GUI を実装する必要はない．
あくまで API サーバーを評価の対象とする．
また，使用する言語は Python 以外でも構わない．

