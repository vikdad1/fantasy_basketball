#R 

setwd("~/Documents/GitHub/nbaproj_ieor/Vikram/processed_data/")
td_top5 <- read.csv("historical_team_data_top_5.csv")
td_top5_gs <- read.csv("historical_team_data_top_5_gs.csv")
td_top5_adv <- read.csv("historical_team_data_top_5_advanced.csv")
td_all <- read.csv("historical_team_data.csv")

td_top5 <- td_top5[complete.cases(td_top5),]
td_top5_gs <- td_top5_gs[complete.cases(td_top5_gs),]
td_top5_adv <- td_top5_adv[complete.cases(td_top5_adv),]
td_all <- td_all[complete.cases(td_all),]

td_top5 <- td_top5[td_top5$season != 2017,]
td_top5_gs <- td_top5_gs[td_top5_gs$season != 2017,]
td_top5_adv <- td_top5_adv[td_top5_adv$season != 2017,]
td_all <- td_all[td_all$season != 2017,]

#TD ALl
td_all <- td_all[,-which(names(td_all) %in% c('season', 'team_name', 'w', 'l'))]

## 75% of the sample size
smp_size <- floor(0.7 * nrow(td_all))

## set the seed to make your partition reproductible
set.seed(100)
train_ind <- sample(seq_len(nrow(td_all)), size = smp_size)

train <- td_all[rownames(td_all) %in% train_ind, ]
test <- td_all[-train_ind, ]

mod_all <- lm(wp~., data=train)

#TD Top 5
td_top5 <- td_top5[,-which(names(td_top5) %in% c('season', 'team_name', 'w', 'l'))]

## 75% of the sample size
smp_size <- floor(0.7 * nrow(td_top5))

## set the seed to make your partition reproductible
set.seed(100)
train_ind <- sample(seq_len(nrow(td_top5)), size = smp_size)

train <- td_top5[rownames(td_top5) %in% train_ind, ]
test <- td_top5[-train_ind, ]

mod_top5 <- lm(wp~., data=train)

#Age, turnovers, blocks, steals ... turnover having a negative coefficient

#TD Top 5 GS
td_top5_gs <- td_top5_gs[,-which(names(td_top5_gs) %in% c('season', 'team_name', 'w', 'l'))]

## 75% of the sample size
smp_size <- floor(0.7 * nrow(td_top5_gs))

## set the seed to make your partition reproductible
set.seed(100)
train_ind <- sample(seq_len(nrow(td_top5_gs)), size = smp_size)

train <- td_top5_gs[rownames(td_top5_gs) %in% train_ind, ]
test <- td_top5_gs[-train_ind, ]

mod_top5_gs <- lm(wp~., data=train)

#Age, blocks, turnovers, again

td_top5_gs <- td_top5_gs[,-which(names(td_top5_gs) %in% c('season', 'team_name', 'w', 'l'))]

## 75% of the sample size
smp_size <- floor(0.7 * nrow(td_top5_gs))

## set the seed to make your partition reproductible
set.seed(100)
train_ind <- sample(seq_len(nrow(td_top5_gs)), size = smp_size)

train <- td_top5_gs[rownames(td_top5_gs) %in% train_ind, ]
test <- td_top5_gs[-train_ind, ]

mod_top5_gs <- lm(wp~., data=train)

###This will be with season averages adjustment
td_top5_adv <- td_top5_adv[,-which(names(td_top5_adv) %in% c('season', 'team_name', 'w', 'l'))]

## 75% of the sample size
smp_size <- floor(0.7 * nrow(td_top5_adv))

## set the seed to make your partition reproductible
set.seed(100)
train_ind <- sample(seq_len(nrow(td_top5_adv)), size = smp_size)

train <- td_top5_adv[rownames(td_top5_adv) %in% train_ind, ]
test <- td_top5_adv[-train_ind, ]

mod_top5_adv <- lm(wp~., data=train)

#Win Shares per 48 minutes, Usage %, Assists %, Per, Personal Fouls 